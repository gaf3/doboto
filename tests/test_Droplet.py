"""
This module contains tests for the main DO class
"""

from unittest import TestCase
from mock import MagicMock, patch, call
from doboto import Droplet
from doboto.DOBOTOException import DOBOTOException


class TestDroplet(TestCase):

    """
    This class implements unittests for the main DO class
    """

    def setUp(self):
        """
        Define resources usable by all unit tests
        """

        self.test_url = "http://abc.example.com"
        self.test_uri = "{}/droplets".format(self.test_url)
        self.test_reports = "{}/reports".format(self.test_url)
        self.test_do = "do"
        self.test_token = "abc123"
        self.test_agent = "Unit"
        self.instantiate_args = (self.test_do, self.test_token, self.test_url, self.test_agent)

        self.klass_name = "Droplet"
        self.klass = getattr(Droplet, self.klass_name)

    def test_class_exists(self):
        """
        Droplet class is defined
        """

        self.assertTrue(hasattr(Droplet, self.klass_name))

    def test_can_instantiate(self):
        """
        Droplet class can be instantiated
        """

        exc_thrown = False

        try:
            self.klass(*self.instantiate_args)
        except Exception:
            exc_thrown = True

        self.assertFalse(exc_thrown)

    @patch('doboto.Droplet.Droplet.pages')
    def test_list(self, mock_pages):
        """
        list works with droplet id
        """

        drop = self.klass(*self.instantiate_args)

        tag_name = "rando_tag"

        drop.list()
        mock_pages.assert_called_with(self.test_uri, "droplets")

        drop.list(tag_name=tag_name)
        drop_uri = "{}?tag_name={}".format(self.test_uri, tag_name)
        mock_pages.assert_called_with(drop_uri, "droplets")

    @patch('doboto.Droplet.Droplet.pages')
    def test_neighbor_list(self, mock_pages):
        """
        neighbors works with droplet id
        """

        id = 12345
        drop = self.klass(*self.instantiate_args)
        drop.neighbor_list(id)
        test_uri = "{}/{}/neighbors".format(self.test_uri, id)

        mock_pages.assert_called_with(test_uri, "droplets")

    @patch('doboto.Droplet.Droplet.pages')
    def test_droplet_neighbor_list(self, mock_pages):
        """
        neighbors works alone
        """

        drop = self.klass(*self.instantiate_args)
        drop.droplet_neighbor_list()
        test_uri = "{}/droplet_neighbors".format(self.test_reports)

        mock_pages.assert_called_with(test_uri, "neighbors")

    def test_ready(self):
        """
        ready checks a droplet's status and tags
        """

        drop = self.klass(*self.instantiate_args)

        self.assertTrue(drop.ready({"id": 1, "status": "old"}, {}))
        self.assertFalse(drop.ready({"status": "new"}, {}))
        self.assertTrue(drop.ready({"status": "old"}, {}))
        self.assertTrue(drop.ready(
            {"status": "old", "networks": {"v4": [{"type": "private"}, {"type": "public"}]}},
            {"private_networking": True}
        ))
        self.assertFalse(drop.ready(
            {"status": "old", "networks": {"v4": []}},
            {"private_networking": True}
        ))
        self.assertFalse(drop.ready(
            {"status": "old", "networks": {}},
            {"ipv6": True}
        ))
        self.assertTrue(drop.ready(
            {"status": "old", "networks": {"v6": []}},
            {"ipv6": True}
        ))
        self.assertFalse(drop.ready(
            {"status": "old", "tags": []},
            {"tags": [1]}
        ))
        self.assertTrue(drop.ready(
            {"status": "old", "tags": [1]},
            {"tags": [1]}
        ))
        self.assertTrue(drop.ready(
            {"id": 1, "status": "old", "networks": {"v6": [], "v4": [{"type": "private"}, ]}},
            {"ipv6": True, "private_networking": True}
        ))

    @patch('time.sleep')
    @patch('doboto.Droplet.Droplet.request')
    def test_create(self, mock_request, mock_sleep):
        """
        create works with name or names
        """

        drop = self.klass(*self.instantiate_args)

        drop.ready = MagicMock(side_effect=[False, False, True])
        drop.info = MagicMock(side_effect=[Exception("Not yet"), {"stuff": "things"}])

        mock_request.return_value = {"id": 1, "people": "stuff"}

        datas = {"name": "test.com", "region": "nyc3",
                 "size": "512mb", "image": "ubuntu-14-04-x64"}
        self.assertEqual(drop.create(datas, wait=True, poll=2), {"stuff": "things"})

        mock_request.assert_called_with(self.test_uri, "droplet", 'POST', attribs=datas)
        mock_sleep.assert_has_calls([call(2), call(2)])
        drop.ready.assert_has_calls([
            call({"id": 1, "people": "stuff"}),
            call({"id": 1, "people": "stuff"}),
            call({"stuff": "things"})
        ])
        drop.info.assert_has_calls([call(1), call(1)])

        mock_request.return_value = {"id": 2, "people": "stuff"}
        drop.ready.side_effect = [False]

        with self.assertRaises(DOBOTOException):
            drop.create(datas, wait=True, poll=4, timeout=-1)

        mock_request.assert_called_with(self.test_uri, "droplet", 'POST', attribs=datas)
        mock_sleep.assert_has_calls([call(4)])
        drop.ready.assert_has_calls([
            call({"id": 2, "people": "stuff"})
        ])
        drop.info.assert_has_calls([call(2)])

        drop.ready.side_effect = [False, False, True]
        drop.info.side_effect = [Exception("Not yet"), {"stuff": "things"}]

        mock_request.return_value = [{"id": 3, "people": "stuff"}]

        datas = {"names": ["test.com", "pass.com", "fail.com"], "region": "nyc3",
                 "size": "512mb", "image": "ubuntu-14-04-x64"}
        self.assertEqual(drop.create(datas, wait=True, poll=5), [{"stuff": "things"}])

        mock_request.assert_called_with(self.test_uri, "droplets", 'POST', attribs=datas)
        mock_sleep.assert_has_calls([call(5), call(5)])
        drop.ready.assert_has_calls([
            call({"id": 3, "people": "stuff"}),
            call({"id": 3, "people": "stuff"}),
            call({"stuff": "things"})
        ])
        drop.info.assert_has_calls([call(3), call(3)])

        drop.ready.side_effect = [False, False, False, False, True]
        drop.info.side_effect = [Exception("Not yet"), {"stuff": "things"}]

        with self.assertRaises(DOBOTOException):
            drop.create(datas, wait=True, timeout=-1)

        with self.assertRaises(ValueError):
            drop.create({})

    def test_present(self):
        """
        present works with name or names
        """

        drop = self.klass(*self.instantiate_args)

        drop.list = MagicMock(return_value=[
            {"id": 1, "name": "people"},
            {"id": 2, "name": "stuff"},
            {"id": 3, "name": "things"}
        ])

        ids = [4, 5, 6, 7]

        def create(attribs, wait, poll, timeout):
            if "name" in attribs:
                return {"id": ids.pop(0), "name": attribs["name"]}
            elif "names" in attribs:
                return [{"id": ids.pop(0), "name": name} for name in attribs["names"]]

        drop.create = MagicMock(side_effect=create)

        exist = drop.present({"name": "people"}, wait=True, poll=2, timeout=3)
        self.assertEqual(exist, ({"id": 1, "name": "people"}, None))

        new = drop.present({"name": "dogs"}, wait=True, poll=2, timeout=3)
        self.assertEqual(new, ({"id": 4, "name": "dogs"}, {"id": 4, "name": "dogs"}))
        drop.create.assert_has_calls([
            call({"name": "dogs"}, True, 2, 3),
        ])

        exists = drop.present({"names": ["stuff", "people"]}, wait=True, poll=4, timeout=5)
        self.assertEqual(exists, (
            [
                {"id": 2, "name": "stuff"},
                {"id": 1, "name": "people"}
            ],
            []
        ))

        news = drop.present({"names": ["cats", "kids"]}, wait=True, poll=4, timeout=5)
        self.assertEqual(news, (
            [
                {"id": 5, "name": "cats"},
                {"id": 6, "name": "kids"}
            ],
            [
                {"id": 5, "name": "cats"},
                {"id": 6, "name": "kids"}
            ]
        ))
        drop.create.assert_has_calls([
            call({"names": ["cats", "kids"]}, True, 4, 5),
        ])

        mixed = drop.present({"names": ["pets", "things"]}, wait=True, poll=6, timeout=7)
        self.assertEqual(mixed, (
            [
                {"id": 7, "name": "pets"},
                {"id": 3, "name": "things"}
            ],
            [
                {"id": 7, "name": "pets"}
            ]
        ))
        drop.create.assert_has_calls([
            call({"names": ["pets"]}, True, 6, 7),
        ])

        drop.create = MagicMock(return_value=[{"name": "something"}])

        with self.assertRaises(DOBOTOException):
            drop.present({"names": ["nothing"]})

        with self.assertRaises(ValueError):
            drop.present({})

    @patch('doboto.Droplet.Droplet.request')
    def test_info(self, mock_request):
        """
        info works with droplet id
        """

        id = 12345
        drop = self.klass(*self.instantiate_args)
        drop.info(id)

        test_uri = "{}/{}".format(self.test_uri, id)
        mock_request.assert_called_with(test_uri, "droplet")

    @patch('doboto.Droplet.Droplet.request')
    def test_destroy(self, mock_request):
        """
        destroy works with droplet id
        """

        id = 12345
        drop = self.klass(*self.instantiate_args)
        drop.destroy(id)
        test_uri = "{}/{}".format(self.test_uri, id)

        mock_request.assert_called_with(test_uri, request_method='DELETE')

        tag_name = "rando-tag"
        drop.destroy(tag_name=tag_name)
        test_uri = "{}?tag_name={}".format(self.test_uri, tag_name)

        mock_request.assert_called_with(test_uri, request_method='DELETE')

        with self.assertRaises(ValueError):
            drop.destroy()

    @patch('doboto.Droplet.Droplet.actions_result')
    @patch('doboto.Droplet.Droplet.action_result')
    @patch('doboto.Droplet.Droplet.request')
    def test_action(self, mock_request, mock_action_result, mock_actions_result):
        """
        action works with droplet id or tag name and needs an action
        """

        mock_request.return_value = {}

        id = 12345
        drop = self.klass(*self.instantiate_args)
        drop.action(id=id, type='test', wait=True, poll=2, timeout=3)
        test_uri = "{}/{}/actions".format(self.test_uri, id)

        mock_request.assert_called_with(test_uri, "action", 'POST', attribs={"type": "test"})
        mock_action_result.assert_called_with({}, True, 2, 3)

        mock_request.return_value = []

        tag_name = "rando-tag"
        drop.action(
            tag_name=tag_name, type='test', attribs={"extra": True},
            wait=True, poll=4, timeout=5
        )
        test_uri = "{}/actions?tag_name={}".format(self.test_uri, tag_name)

        mock_request.assert_called_with(
            test_uri, "actions", 'POST', attribs={"type": "test", "extra": True}
        )
        mock_actions_result.assert_called_with([], True, 4, 5)

        with self.assertRaises(ValueError):
            drop.action()

        with self.assertRaises(ValueError):
            drop.action(type='stuff')

    @patch('doboto.Droplet.Droplet.pages')
    def test_backup_list(self, mock_pages):
        """
        backups works with droplet id
        """

        id = 12345
        drop = self.klass(*self.instantiate_args)
        drop.backup_list(id)
        test_uri = "{}/{}/backups".format(self.test_uri, id)

        mock_pages.assert_called_with(test_uri, "backups")

    @patch('doboto.Droplet.Droplet.action')
    def test_backup_enable(self, mock_action):
        """
        backup_enable works with droplet id or tag name
        """

        id = 12345
        drop = self.klass(*self.instantiate_args)
        drop.backup_enable(id=id, wait=True, poll=2, timeout=3)

        mock_action.assert_called_with(
            id=id, tag_name=None, type="enable_backups",
            wait=True, poll=2, timeout=3
        )

        tag_name = "rando-tag"
        drop.backup_enable(tag_name=tag_name, wait=True, poll=4, timeout=5)

        mock_action.assert_called_with(
            id=None, tag_name='rando-tag', type="enable_backups",
            wait=True, poll=4, timeout=5
        )

    @patch('doboto.Droplet.Droplet.action')
    def test_backups_disable(self, mock_action):
        """
        backups_disable works with droplet id or tag name
        """

        id = 12345
        drop = self.klass(*self.instantiate_args)
        drop.backup_disable(id=id, wait=True, poll=2, timeout=3)

        mock_action.assert_called_with(
            id=id, tag_name=None, type="disable_backups",
            wait=True, poll=2, timeout=3
        )

        tag_name = "rando-tag"
        drop.backup_disable(tag_name=tag_name, wait=True, poll=4, timeout=5)

        mock_action.assert_called_with(
            id=None, tag_name='rando-tag', type="disable_backups",
            wait=True, poll=4, timeout=5
        )

    @patch('doboto.Droplet.Droplet.action_result')
    @patch('doboto.Droplet.Droplet.request')
    def test_reboot(self, mock_request, mock_action_result):
        """
        test that reboot works with id and action
        """
        drop = self.klass(*self.instantiate_args)

        mock_request.return_value = {}

        id = 12345
        test_uri = "{}/{}/actions".format(self.test_uri, id)
        datas = {"type": "reboot"}

        drop.reboot(id, wait=True, poll=2, timeout=3)

        mock_request.assert_called_with(test_uri, "action", 'POST', attribs=datas)
        mock_action_result.assert_called_with({}, True, 2, 3)

    @patch('doboto.Droplet.Droplet.action')
    def test_shutdown(self, mock_action):
        """
        shutdown works with droplet id or tag name
        """

        id = 12345
        drop = self.klass(*self.instantiate_args)
        drop.shutdown(id=id, wait=True, poll=2, timeout=3)

        mock_action.assert_called_with(
            id=id, tag_name=None, type="shutdown",
            wait=True, poll=2, timeout=3
        )

        tag_name = "rando-tag"
        drop.shutdown(tag_name=tag_name, wait=True, poll=4, timeout=5)

        mock_action.assert_called_with(
            id=None, tag_name='rando-tag', type="shutdown",
            wait=True, poll=4, timeout=5
        )

    @patch('doboto.Droplet.Droplet.action')
    def test_power_on(self, mock_action):
        """
        power_on works with droplet id or tag name
        """

        id = 12345
        drop = self.klass(*self.instantiate_args)
        drop.power_on(id=id, wait=True, poll=2, timeout=3)

        mock_action.assert_called_with(
            id=id, tag_name=None, type="power_on",
            wait=True, poll=2, timeout=3
        )

        tag_name = "rando-tag"
        drop.power_on(tag_name=tag_name, wait=True, poll=4, timeout=5)

        mock_action.assert_called_with(
            id=None, tag_name='rando-tag', type="power_on",
            wait=True, poll=4, timeout=5
        )

    @patch('doboto.Droplet.Droplet.action')
    def test_power_off(self, mock_action):
        """
        power_off works with droplet id or tag name
        """

        id = 12345
        drop = self.klass(*self.instantiate_args)
        drop.power_off(id=id, wait=True, poll=2, timeout=3)

        mock_action.assert_called_with(
            id=id, tag_name=None, type="power_off",
            wait=True, poll=2, timeout=3
        )

        tag_name = "rando-tag"
        drop.power_off(tag_name=tag_name, wait=True, poll=4, timeout=5)

        mock_action.assert_called_with(
            id=None, tag_name='rando-tag', type="power_off",
            wait=True, poll=4, timeout=5
        )

    @patch('doboto.Droplet.Droplet.action')
    def test_power_cycle(self, mock_action):
        """
        power_cycle works with droplet id or tag name
        """

        id = 12345
        drop = self.klass(*self.instantiate_args)
        drop.power_cycle(id=id, wait=True, poll=2, timeout=3)

        mock_action.assert_called_with(
            id=id, tag_name=None, type="power_cycle",
            wait=True, poll=2, timeout=3
        )

        tag_name = "rando-tag"
        drop.power_cycle(tag_name=tag_name, wait=True, poll=4, timeout=5)

        mock_action.assert_called_with(
            id=None, tag_name='rando-tag', type="power_cycle",
            wait=True, poll=4, timeout=5
        )

    @patch('doboto.Droplet.Droplet.action_result')
    @patch('doboto.Droplet.Droplet.request')
    def test_restore(self, mock_request, mock_action_result):
        """
        test that restore commands with id and image
        """
        drop = self.klass(*self.instantiate_args)
        id = 12345
        test_uri = "{}/{}/actions".format(self.test_uri, id)

        mock_request.return_value = {}

        image = 654321
        datas = {"type": "restore", "image": image}
        drop.restore(id, image, wait=True, poll=2, timeout=3)
        mock_request.assert_called_with(test_uri, "action", 'POST', attribs=datas)
        mock_action_result.assert_called_with({}, True, 2, 3)

        image = "my-image-slug"
        datas = {"type": "restore", "image": "%s" % (image)}
        drop.restore(id, image)
        mock_request.assert_called_with(test_uri, "action", 'POST', attribs=datas)

    @patch('doboto.Droplet.Droplet.action_result')
    @patch('doboto.Droplet.Droplet.request')
    def test_password_reset(self, mock_request, mock_action_result):
        """
        test password_reset works with droplet id
        """
        drop = self.klass(*self.instantiate_args)
        id = 12345
        test_uri = "{}/{}/actions".format(self.test_uri, id)

        mock_request.return_value = {}

        datas = {"type": "password_reset"}
        drop.password_reset(id, wait=True, poll=2, timeout=3)
        mock_request.assert_called_with(test_uri, "action", 'POST', attribs=datas)
        mock_action_result.assert_called_with({}, True, 2, 3)

    @patch('doboto.Droplet.Droplet.action_result')
    @patch('doboto.Droplet.Droplet.request')
    def test_resize(self, mock_request, mock_action_result):
        """
        test resize works with droplet id, size, and optionally disk resize flag
        """
        drop = self.klass(*self.instantiate_args)
        id = 12345
        test_uri = "{}/{}/actions".format(self.test_uri, id)

        mock_request.return_value = {}

        # test with size and not specify disk
        size = "32gb"
        datas = {"type": "resize", "size": "%s" % (size), "disk": "false"}
        drop.resize(id, size, wait=True, poll=2, timeout=3)
        mock_request.assert_called_with(test_uri, "action", 'POST', attribs=datas)
        mock_action_result.assert_called_with({}, True, 2, 3)

        # test with size and specify disk
        size = "16gb"
        disk = True
        datas = {"type": "resize", "size": "%s" % (size), "disk": "true"}
        drop.resize(id, size, disk)
        mock_request.assert_called_with(test_uri, "action", 'POST', attribs=datas)

    @patch('doboto.Droplet.Droplet.action_result')
    @patch('doboto.Droplet.Droplet.request')
    def test_rebuild(self, mock_request, mock_action_result):
        """
        test rebuild works with droplet id, image
        """
        drop = self.klass(*self.instantiate_args)
        id = 12345
        test_uri = "{}/{}/actions".format(self.test_uri, id)

        mock_request.return_value = {}

        # test with image id
        image = 654321
        datas = {"type": "rebuild", "image": image}
        drop.rebuild(id, image, wait=True, poll=2, timeout=3)
        mock_request.assert_called_with(test_uri, "action", 'POST', attribs=datas)
        mock_action_result.assert_called_with({}, True, 2, 3)

        # test with image slug
        image = "my-image-slug"
        datas = {"type": "rebuild", "image": "%s" % (image)}
        drop.rebuild(id, image)
        mock_request.assert_called_with(test_uri, "action", 'POST', attribs=datas)

    @patch('doboto.Droplet.Droplet.action_result')
    @patch('doboto.Droplet.Droplet.request')
    def test_rename(self, mock_request, mock_action_result):
        """
        test rename works with droplet id, image
        """
        drop = self.klass(*self.instantiate_args)
        id = 12345
        test_uri = "{}/{}/actions".format(self.test_uri, id)

        mock_request.return_value = {}

        # test with image id
        name = "cool-droplet-bruh"
        datas = {"type": "rename", "name": "%s" % (name)}
        drop.rename(id, name, wait=True, poll=2, timeout=3)
        mock_request.assert_called_with(test_uri, "action", 'POST', attribs=datas)
        mock_action_result.assert_called_with({}, True, 2, 3)

    @patch('doboto.Droplet.Droplet.pages')
    def test_kernel_list(self, mock_pages):
        """
        kernel_list works with droplet id
        """

        id = 12345
        drop = self.klass(*self.instantiate_args)
        drop.kernel_list(id)
        test_uri = "{}/{}/kernels".format(self.test_uri, id)

        mock_pages.assert_called_with(test_uri, "kernels")

    @patch('doboto.Droplet.Droplet.action_result')
    @patch('doboto.Droplet.Droplet.request')
    def test_kernel_update(self, mock_request, mock_action_result):
        """
        test kernel_update works with droplet id, kernel id
        """
        drop = self.klass(*self.instantiate_args)
        id = 12345
        test_uri = "{}/{}/actions".format(self.test_uri, id)

        mock_request.return_value = {}

        # test with kernel id
        kernel = 654321
        datas = {"type": "change_kernel", "kernel": kernel}
        drop.kernel_update(id, kernel, wait=True, poll=2, timeout=3)
        mock_request.assert_called_with(test_uri, "action", 'POST', attribs=datas)
        mock_action_result.assert_called_with({}, True, 2, 3)

        # test with kernel as str()
        kernel = "654321"
        datas = {"type": "change_kernel", "kernel": kernel}
        drop.kernel_update(id, kernel)
        mock_request.assert_called_with(test_uri, "action", 'POST', attribs=datas)

    @patch('doboto.Droplet.Droplet.action')
    def test_ipv6_enable(self, mock_action):
        """
        enable_ipv6 works with droplet id or tag name
        """

        id = 12345
        drop = self.klass(*self.instantiate_args)
        drop.ipv6_enable(id=id, wait=True, poll=2, timeout=3)

        mock_action.assert_called_with(
            id=id, tag_name=None, type="enable_ipv6",
            wait=True, poll=2, timeout=3
        )

        tag_name = "rando-tag"
        drop.ipv6_enable(tag_name=tag_name, wait=True, poll=4, timeout=5)

        mock_action.assert_called_with(
            id=None, tag_name='rando-tag', type="enable_ipv6",
            wait=True, poll=4, timeout=5
        )

    @patch('doboto.Droplet.Droplet.action')
    def test_private_networking_enable(self, mock_action):
        """
        private_networking_enable works with droplet id or tag name
        """

        id = 12345
        drop = self.klass(*self.instantiate_args)
        drop.private_networking_enable(id=id, wait=True, poll=2, timeout=3)

        mock_action.assert_called_with(
            id=id, tag_name=None, type="enable_private_networking",
            wait=True, poll=2, timeout=3
        )

        tag_name = "rando-tag"
        drop.private_networking_enable(tag_name=tag_name, wait=True, poll=4, timeout=5)

        mock_action.assert_called_with(
            id=None, tag_name='rando-tag', type="enable_private_networking",
            wait=True, poll=4, timeout=5
        )

    @patch('doboto.Droplet.Droplet.pages')
    def test_snapshot_list(self, mock_pages):
        """
        snapshot_list works with droplet id
        """

        id = 12345
        drop = self.klass(*self.instantiate_args)
        drop.snapshot_list(id)
        test_uri = "{}/{}/snapshots".format(self.test_uri, id)

        mock_pages.assert_called_with(test_uri, "snapshots")

    @patch('doboto.Droplet.Droplet.action')
    def test_snapshot_create(self, mock_action):
        """
        snapshot_create works with droplet id or tag name and name for the snapshot
        """

        id = 12345
        drop = self.klass(*self.instantiate_args)
        drop.snapshot_create(id=id, snapshot_name="test", wait=True, poll=2, timeout=3)

        mock_action.assert_called_with(
            id=id, tag_name=None, type="snapshot", attribs={"name": "test"},
            wait=True, poll=2, timeout=3
        )

        tag_name = "rando-tag"
        drop.snapshot_create(tag_name=tag_name, snapshot_name="test", wait=True, poll=4, timeout=5)

        mock_action.assert_called_with(
            id=None, tag_name='rando-tag', type="snapshot", attribs={"name": "test"},
            wait=True, poll=4, timeout=5
        )

        with self.assertRaises(ValueError):
            drop.snapshot_create(id=0)

    @patch('doboto.Droplet.Droplet.pages')
    def test_action_list(self, mock_pages):
        """
        action_list works with droplet id
        """

        id = 12345
        drop = self.klass(*self.instantiate_args)
        drop.action_list(id)
        test_uri = "{}/{}/actions".format(self.test_uri, id)

        mock_pages.assert_called_with(test_uri, "actions")

    @patch('doboto.Droplet.Droplet.request')
    def test_action_info(self, mock_request):
        """
        action_info works with droplet id
        """

        id = 12345
        action_id = 54321
        drop = self.klass(*self.instantiate_args)
        drop.action_info(id, action_id)
        test_uri = "{}/{}/actions/{}".format(
            self.test_uri, id, action_id)

        mock_request.assert_called_with(test_uri, "action")
