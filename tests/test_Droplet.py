"""
This module contains tests for the main DO class
"""

from unittest import TestCase
from mock import MagicMock, patch
from doboto import Droplet


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
        self.test_token = "abc123"
        self.instantiate_args = (self.test_url, self.test_token)

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

    @patch('doboto.Droplet.Droplet.make_request')
    def test_list(self, mock_make_request):
        """
        list works with droplet id
        """

        drop = self.klass(self.test_url, self.test_token)

        tag_name = "rando_tag"

        drop.list()
        mock_make_request.assert_called_with(self.test_uri)

        drop.list(tag_name=tag_name)
        drop_uri = "{}?tag_name={}".format(self.test_uri, tag_name)
        mock_make_request.assert_called_with(drop_uri)

    @patch('doboto.Droplet.Droplet.make_request')
    def test_neighbor_list(self, mock_make_request):
        """
        neighbors works with droplet id
        """

        id = 12345
        drop = self.klass(self.test_url, self.test_token)
        drop.neighbor_list(id)
        test_uri = "{}/{}/neighbors".format(self.test_uri, id)

        mock_make_request.assert_called_with(test_uri)

    @patch('doboto.Droplet.Droplet.make_request')
    def test_droplet_neighbor_list(self, mock_make_request):
        """
        neighbors works alone
        """

        drop = self.klass(self.test_url, self.test_token)
        drop.droplet_neighbor_list()
        test_uri = "{}/droplet_neighbors".format(self.test_reports)

        mock_make_request.assert_called_with(test_uri)

    @patch('doboto.Droplet.Droplet.make_request')
    def test_create(self, mock_make_request):
        """
        create works with droplet id
        """

        drop = self.klass(self.test_url, self.test_token)
        datas = {"name": "test.com", "region": "nyc3",
                 "size": "512mb", "image": "ubuntu-14-04-x64"}
        drop.create(datas)

        mock_make_request.assert_called_with(
            self.test_uri, 'POST', attribs=datas)

        # Check empty

        drop.create()

        mock_make_request.assert_called_with(
            self.test_uri, 'POST', attribs={})

    @patch('doboto.Droplet.Droplet.make_request')
    def test_info(self, mock_make_request):
        """
        info works with droplet id
        """

        id = 12345
        drop = self.klass(self.test_url, self.test_token)
        drop.info(id)

        test_uri = "{}/{}".format(self.test_uri, id)
        mock_make_request.assert_called_with(test_uri)

    @patch('doboto.Droplet.Droplet.make_request')
    def test_destroy(self, mock_make_request):
        """
        destroy works with droplet id
        """

        id = 12345
        drop = self.klass(self.test_url, self.test_token)
        drop.destroy(id)
        test_uri = "{}/{}".format(self.test_uri, id)

        mock_make_request.assert_called_with(test_uri, 'DELETE')

        tag_name = "rando-tag"
        drop.destroy(tag_name=tag_name)
        test_uri = "{}?tag_name={}".format(self.test_uri, tag_name)

        mock_make_request.assert_called_with(test_uri, 'DELETE')

        with self.assertRaises(ValueError):
            drop.destroy()

    @patch('doboto.Droplet.Droplet.make_request')
    def test_action(self, mock_make_request):
        """
        action works with droplet id or tag name and needs an action
        """

        id = 12345
        drop = self.klass(self.test_url, self.test_token)
        drop.action(id=id, type='test')
        test_uri = "{}/{}/actions".format(self.test_uri, id)

        mock_make_request.assert_called_with(test_uri, 'POST', attribs={"type": "test"})

        tag_name = "rando-tag"
        drop.action(tag_name=tag_name, type='test', attribs={"extra": True})
        test_uri = "{}/actions?tag_name={}".format(self.test_uri, tag_name)

        mock_make_request.assert_called_with(
            test_uri, 'POST', attribs={"type": "test", "extra": True}
        )

        with self.assertRaises(ValueError):
            drop.action()

        with self.assertRaises(ValueError):
            drop.action(id=0)

    @patch('doboto.Droplet.Droplet.make_request')
    def test_backup_list(self, mock_make_request):
        """
        backups works with droplet id
        """

        id = 12345
        drop = self.klass(self.test_url, self.test_token)
        drop.backup_list(id)
        test_uri = "{}/{}/backups".format(self.test_uri, id)

        mock_make_request.assert_called_with(test_uri)

    @patch('doboto.Droplet.Droplet.action')
    def test_backup_enable(self, mock_action):
        """
        backup_enable works with droplet id or tag name
        """

        id = 12345
        drop = self.klass(self.test_url, self.test_token)
        drop.backup_enable(id=id)

        mock_action.assert_called_with(id=id, tag_name=None, type="enable_backups")

        tag_name = "rando-tag"
        drop.backup_enable(tag_name=tag_name)

        mock_action.assert_called_with(id=None, tag_name='rando-tag', type="enable_backups")

    @patch('doboto.Droplet.Droplet.action')
    def test_backups_disable(self, mock_action):
        """
        backups_disable works with droplet id or tag name
        """

        id = 12345
        drop = self.klass(self.test_url, self.test_token)
        drop.backup_disable(id=id)

        mock_action.assert_called_with(id=id, tag_name=None, type="disable_backups")

        tag_name = "rando-tag"
        drop.backup_disable(tag_name=tag_name)

        mock_action.assert_called_with(id=None, tag_name='rando-tag', type="disable_backups")

    @patch('doboto.Droplet.Droplet.make_request')
    def test_reboot(self, mock_make_request):
        """
        test that reboot works with id and action
        """
        drop = self.klass(self.test_url, self.test_token)

        id = 12345
        test_uri = "{}/{}/actions".format(self.test_uri, id)
        datas = {"type": "reboot"}

        drop.reboot(id)

        mock_make_request.assert_called_with(test_uri, 'POST', attribs=datas)

    @patch('doboto.Droplet.Droplet.action')
    def test_shutdown(self, mock_action):
        """
        shutdown works with droplet id or tag name
        """

        id = 12345
        drop = self.klass(self.test_url, self.test_token)
        drop.shutdown(id=id)

        mock_action.assert_called_with(id=id, tag_name=None, type="shutdown")

        tag_name = "rando-tag"
        drop.shutdown(tag_name=tag_name)

        mock_action.assert_called_with(id=None, tag_name='rando-tag', type="shutdown")

    @patch('doboto.Droplet.Droplet.action')
    def test_power_on(self, mock_action):
        """
        power_on works with droplet id or tag name
        """

        id = 12345
        drop = self.klass(self.test_url, self.test_token)
        drop.power_on(id=id)

        mock_action.assert_called_with(id=id, tag_name=None, type="power_on")

        tag_name = "rando-tag"
        drop.power_on(tag_name=tag_name)

        mock_action.assert_called_with(id=None, tag_name='rando-tag', type="power_on")

    @patch('doboto.Droplet.Droplet.action')
    def test_power_off(self, mock_action):
        """
        power_off works with droplet id or tag name
        """

        id = 12345
        drop = self.klass(self.test_url, self.test_token)
        drop.power_off(id=id)

        mock_action.assert_called_with(id=id, tag_name=None, type="power_off")

        tag_name = "rando-tag"
        drop.power_off(tag_name=tag_name)

        mock_action.assert_called_with(id=None, tag_name='rando-tag', type="power_off")

    @patch('doboto.Droplet.Droplet.action')
    def test_power_cycle(self, mock_action):
        """
        power_cycle works with droplet id or tag name
        """

        id = 12345
        drop = self.klass(self.test_url, self.test_token)
        drop.power_cycle(id=id)

        mock_action.assert_called_with(id=id, tag_name=None, type="power_cycle")

        tag_name = "rando-tag"
        drop.power_cycle(tag_name=tag_name)

        mock_action.assert_called_with(id=None, tag_name='rando-tag', type="power_cycle")

    @patch('doboto.Droplet.Droplet.make_request')
    def test_restore(self, mock_make_request):
        """
        test that restore commands with id and image
        """
        drop = self.klass(self.test_url, self.test_token)
        id = 12345
        test_uri = "{}/{}/actions".format(self.test_uri, id)

        image = 654321
        datas = {"type": "restore", "image": image}
        drop.restore(id, image)
        mock_make_request.assert_called_with(test_uri, 'POST', attribs=datas)

        image = "my-image-slug"
        datas = {"type": "restore", "image": "%s" % (image)}
        drop.restore(id, image)
        mock_make_request.assert_called_with(test_uri, 'POST', attribs=datas)

    @patch('doboto.Droplet.Droplet.make_request')
    def test_password_reset(self, mock_make_request):
        """
        test password_reset works with droplet id
        """
        drop = self.klass(self.test_url, self.test_token)
        id = 12345
        test_uri = "{}/{}/actions".format(self.test_uri, id)

        datas = {"type": "password_reset"}
        drop.password_reset(id)
        mock_make_request.assert_called_with(test_uri, 'POST', attribs=datas)

    @patch('doboto.Droplet.Droplet.make_request')
    def test_resize(self, mock_make_request):
        """
        test resize works with droplet id, size, and optionally disk resize flag
        """
        drop = self.klass(self.test_url, self.test_token)
        id = 12345
        test_uri = "{}/{}/actions".format(self.test_uri, id)

        # test with size and not specify disk
        size = "32gb"
        datas = {"type": "resize", "size": "%s" % (size), "disk": "false"}
        drop.resize(id, size)
        mock_make_request.assert_called_with(test_uri, 'POST', attribs=datas)

        # test with size and specify disk
        size = "16gb"
        disk = True
        datas = {"type": "resize", "size": "%s" % (size), "disk": "true"}
        drop.resize(id, size, disk)
        mock_make_request.assert_called_with(test_uri, 'POST', attribs=datas)

    @patch('doboto.Droplet.Droplet.make_request')
    def test_rebuild(self, mock_make_request):
        """
        test rebuild works with droplet id, image
        """
        drop = self.klass(self.test_url, self.test_token)
        id = 12345
        test_uri = "{}/{}/actions".format(self.test_uri, id)

        # test with image id
        image = 654321
        datas = {"type": "rebuild", "image": image}
        drop.rebuild(id, image)
        mock_make_request.assert_called_with(test_uri, 'POST', attribs=datas)

        # test with image slug
        image = "my-image-slug"
        datas = {"type": "rebuild", "image": "%s" % (image)}
        drop.rebuild(id, image)
        mock_make_request.assert_called_with(test_uri, 'POST', attribs=datas)

    @patch('doboto.Droplet.Droplet.make_request')
    def test_rename(self, mock_make_request):
        """
        test rename works with droplet id, image
        """
        drop = self.klass(self.test_url, self.test_token)
        id = 12345
        test_uri = "{}/{}/actions".format(self.test_uri, id)

        # test with image id
        name = "cool-droplet-bruh"
        datas = {"type": "rename", "name": "%s" % (name)}
        drop.rename(id, name)
        mock_make_request.assert_called_with(test_uri, 'POST', attribs=datas)

    @patch('doboto.Droplet.Droplet.make_request')
    def test_kernel_list(self, mock_make_request):
        """
        kernel_list works with droplet id
        """

        id = 12345
        drop = self.klass(self.test_url, self.test_token)
        drop.kernel_list(id)
        test_uri = "{}/{}/kernels".format(self.test_uri, id)

        mock_make_request.assert_called_with(test_uri)

    @patch('doboto.Droplet.Droplet.make_request')
    def test_kernel_update(self, mock_make_request):
        """
        test kernel_update works with droplet id, kernel id
        """
        drop = self.klass(self.test_url, self.test_token)
        id = 12345
        test_uri = "{}/{}/actions".format(self.test_uri, id)

        # test with kernel id
        kernel = 654321
        datas = {"type": "change_kernel", "kernel": kernel}
        drop.kernel_update(id, kernel)
        mock_make_request.assert_called_with(test_uri, 'POST', attribs=datas)

        # test with kernel as str()
        kernel = "654321"
        datas = {"type": "change_kernel", "kernel": kernel}
        drop.kernel_update(id, kernel)
        mock_make_request.assert_called_with(test_uri, 'POST', attribs=datas)

    @patch('doboto.Droplet.Droplet.action')
    def test_ipv6_enable(self, mock_action):
        """
        enable_ipv6 works with droplet id or tag name
        """

        id = 12345
        drop = self.klass(self.test_url, self.test_token)
        drop.ipv6_enable(id=id)

        mock_action.assert_called_with(id=id, tag_name=None, type="enable_ipv6")

        tag_name = "rando-tag"
        drop.ipv6_enable(tag_name=tag_name)

        mock_action.assert_called_with(id=None, tag_name='rando-tag', type="enable_ipv6")

    @patch('doboto.Droplet.Droplet.action')
    def test_private_networking_enable(self, mock_action):
        """
        private_networking_enable works with droplet id or tag name
        """

        id = 12345
        drop = self.klass(self.test_url, self.test_token)
        drop.private_networking_enable(id=id)

        mock_action.assert_called_with(id=id, tag_name=None, type="enable_private_networking")

        tag_name = "rando-tag"
        drop.private_networking_enable(tag_name=tag_name)

        mock_action.assert_called_with(
            id=None, tag_name='rando-tag', type="enable_private_networking"
        )

    @patch('doboto.Droplet.Droplet.make_request')
    def test_snapshot_list(self, mock_make_request):
        """
        snapshot_list works with droplet id
        """

        id = 12345
        drop = self.klass(self.test_url, self.test_token)
        drop.snapshot_list(id)
        test_uri = "{}/{}/snapshots".format(self.test_uri, id)

        mock_make_request.assert_called_with(test_uri)

    @patch('doboto.Droplet.Droplet.action')
    def test_snapshot_create(self, mock_action):
        """
        snapshot_create works with droplet id or tag name and name for the snapshot
        """

        id = 12345
        drop = self.klass(self.test_url, self.test_token)
        drop.snapshot_create(id=id, name="test")

        mock_action.assert_called_with(
            id=id, tag_name=None, type="snapshot", attribs={"name": "test"}
        )

        tag_name = "rando-tag"
        drop.snapshot_create(tag_name=tag_name, name="test")

        mock_action.assert_called_with(
            id=None, tag_name='rando-tag', type="snapshot", attribs={"name": "test"}
        )

        with self.assertRaises(ValueError):
            drop.snapshot_create(id=0)

    @patch('doboto.Droplet.Droplet.make_request')
    def test_action_list(self, mock_make_request):
        """
        action_list works with droplet id
        """

        id = 12345
        drop = self.klass(self.test_url, self.test_token)
        drop.action_list(id)
        test_uri = "{}/{}/actions".format(self.test_uri, id)

        mock_make_request.assert_called_with(test_uri)

    @patch('doboto.Droplet.Droplet.make_request')
    def test_action_info(self, mock_make_request):
        """
        action_info works with droplet id
        """

        id = 12345
        action_id = 54321
        drop = self.klass(self.test_url, self.test_token)
        drop.action_info(id, action_id)
        test_uri = "{}/{}/actions/{}".format(
            self.test_uri, id, action_id)

        mock_make_request.assert_called_with(test_uri)
