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
    def test_list_kernels(self, mock_make_request):
        """
        list_kernels works with droplet id
        """

        id = 12345
        drop = self.klass(self.test_url, self.test_token)
        drop.list_kernels(id)
        test_uri = "{}/{}/kernels".format(self.test_uri, id)

        mock_make_request.assert_called_with(test_uri)

    @patch('doboto.Droplet.Droplet.make_request')
    def test_list_snapshots(self, mock_make_request):
        """
        list_snapshots works with droplet id
        """

        id = 12345
        drop = self.klass(self.test_url, self.test_token)
        drop.list_snapshots(id)
        test_uri = "{}/{}/snapshots".format(self.test_uri, id)

        mock_make_request.assert_called_with(test_uri)

    @patch('doboto.Droplet.Droplet.make_request')
    def test_list_backups(self, mock_make_request):
        """
        list_backups works with droplet id
        """

        id = 12345
        drop = self.klass(self.test_url, self.test_token)
        drop.list_backups(id)
        test_uri = "{}/{}/backups".format(self.test_uri, id)

        mock_make_request.assert_called_with(test_uri)

    @patch('doboto.Droplet.Droplet.make_request')
    def test_list_actions(self, mock_make_request):
        """
        list_actions works with droplet id
        """

        id = 12345
        drop = self.klass(self.test_url, self.test_token)
        drop.list_actions(id)
        test_uri = "{}/{}/actions".format(self.test_uri, id)

        mock_make_request.assert_called_with(test_uri)

    @patch('doboto.Droplet.Droplet.make_request')
    def test_get_action(self, mock_make_request):
        """
        get_actions works with droplet id
        """

        id = 12345
        action_id = 54321
        drop = self.klass(self.test_url, self.test_token)
        drop.get_action(id, action_id)
        test_uri = "{}/{}/actions/{}".format(
            self.test_uri, id, action_id)

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
    def test_backups(self, mock_make_request):
        """
        test that backups works with id and action
        """
        drop = self.klass(self.test_url, self.test_token)

        id = 12345
        action = "on"
        test_uri = "{}/{}/actions".format(self.test_uri, id)
        datas = {"type": "enable_backups"}

        drop.backups(id, action)

        mock_make_request.assert_called_with(test_uri, 'POST', attribs=datas)

        with self.assertRaises(ValueError):
            drop.backups(id, "bad-action")

        action = "off"
        tag = "rando-tag"
        test_uri = "{}/actions?tag_name={}".format(self.test_uri, tag)
        datas = {"type": "disable_backups"}

        drop.backups("all", action, tag_name=tag)

        mock_make_request.assert_called_with(test_uri, 'POST', attribs=datas)

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

    @patch('doboto.Droplet.Droplet.make_request')
    def test_power(self, mock_make_request):
        """
        test that power commands with id and action
        """
        drop = self.klass(self.test_url, self.test_token)

        id = 12345
        test_uri = "{}/{}/actions".format(self.test_uri, id)

        action = "on"
        datas = {"type": "power_on"}
        drop.power(id, action)
        mock_make_request.assert_called_with(test_uri, 'POST', attribs=datas)

        action = "off"
        datas = {"type": "power_off"}
        drop.power(id, action)
        mock_make_request.assert_called_with(test_uri, 'POST', attribs=datas)

        action = "cycle"
        datas = {"type": "power_cycle"}
        drop.power(id, action)
        mock_make_request.assert_called_with(test_uri, 'POST', attribs=datas)

        # fail with back action
        with self.assertRaises(ValueError):
            drop.power(id, "bad-action")

        # work with tags
        tag = "rando-tag"
        test_uri = "{}/actions?tag_name={}".format(self.test_uri, tag)
        action = "off"
        datas = {"type": "power_off"}
        drop.power("all", action, tag_name=tag)
        mock_make_request.assert_called_with(test_uri, 'POST', attribs=datas)

    @patch('doboto.Droplet.Droplet.make_request')
    def test_shutdown(self, mock_make_request):
        """
        test that power commands with id and action
        """
        drop = self.klass(self.test_url, self.test_token)

        id = 12345
        test_uri = "{}/{}/actions".format(self.test_uri, id)

        datas = {"type": "shutdown"}
        drop.shutdown(id)
        mock_make_request.assert_called_with(test_uri, 'POST', attribs=datas)

        # work with tags
        tag = "rando-tag"
        test_uri = "{}/actions?tag_name={}".format(self.test_uri, tag)
        datas = {"type": "shutdown"}
        drop.shutdown("all", tag_name=tag)
        mock_make_request.assert_called_with(test_uri, 'POST', attribs=datas)

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
    def test_change_kernel(self, mock_make_request):
        """
        test change_kernel works with droplet id, kernel id
        """
        drop = self.klass(self.test_url, self.test_token)
        id = 12345
        test_uri = "{}/{}/actions".format(self.test_uri, id)

        # test with kernel id
        kernel = 654321
        datas = {"type": "change_kernel", "kernel": kernel}
        drop.change_kernel(id, kernel)
        mock_make_request.assert_called_with(test_uri, 'POST', attribs=datas)

        # test with kernel as str()
        kernel = "654321"
        datas = {"type": "change_kernel", "kernel": kernel}
        drop.change_kernel(id, kernel)
        mock_make_request.assert_called_with(test_uri, 'POST', attribs=datas)

    @patch('doboto.Droplet.Droplet.make_request')
    def test_enable_ipv6(self, mock_make_request):
        """
        test enable_ipv6 works with droplet id, kernel id
        """
        drop = self.klass(self.test_url, self.test_token)
        id = 12345
        test_uri = "{}/{}/actions".format(self.test_uri, id)

        # test without tag
        datas = {"type": "enable_ipv6"}
        drop.enable_ipv6(id)
        mock_make_request.assert_called_with(test_uri, 'POST', attribs=datas)

        # test with tag
        tag_name = "rando-tag"
        test_uri = "{}/actions?tag_name={}".format(self.test_uri, tag_name)
        datas = {"type": "enable_ipv6"}
        drop.enable_ipv6("all", tag_name=tag_name)
        mock_make_request.assert_called_with(test_uri, 'POST', attribs=datas)

    @patch('doboto.Droplet.Droplet.make_request')
    def test_enable_private_networking(self, mock_make_request):
        """
        test enable_private_networking works with droplet id, kernel id
        """
        drop = self.klass(self.test_url, self.test_token)
        id = 12345
        test_uri = "{}/{}/actions".format(self.test_uri, id)

        # test without tag
        datas = {"type": "enable_private_networking"}
        drop.enable_private_networking(id)
        mock_make_request.assert_called_with(test_uri, 'POST', attribs=datas)

        # test with tag
        tag = "rando-tag"
        test_uri = "{}/actions?tag_name={}".format(self.test_uri, tag)
        datas = {"type": "enable_private_networking"}
        drop.enable_private_networking("all", tag_name=tag)
        mock_make_request.assert_called_with(test_uri, 'POST', attribs=datas)

    @patch('doboto.Droplet.Droplet.make_request')
    def test_take_snapshot(self, mock_make_request):
        """
        test take_snapshot works with droplet id, kernel id
        """
        drop = self.klass(self.test_url, self.test_token)
        id = 12345
        test_uri = "{}/{}/actions".format(self.test_uri, id)

        # test without tag
        snap_name = "snap-1"
        datas = {"type": "snapshot", "name": "%s" % (snap_name)}
        drop.take_snapshot(id, snap_name)
        mock_make_request.assert_called_with(test_uri, 'POST', attribs=datas)

        # test with tag
        tag = "rando-tag"
        test_uri = "{}/actions?tag_name={}".format(self.test_uri, tag)
        snap_name = "snap-2"
        datas = {"type": "snapshot", "name": "%s" % (snap_name)}
        drop.take_snapshot("all", snap_name, tag_name=tag)
        mock_make_request.assert_called_with(test_uri, 'POST', attribs=datas)
