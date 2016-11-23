"""
This module contains tests for the main DO class
"""

from unittest import TestCase
from mock import MagicMock, patch
from doboto import Volume


class TestVolume(TestCase):

    """
    This class implements unittests for the main DO class
    """

    def setUp(self):
        """
        Define resources usable by all unit tests
        """

        self.test_url = "http://abc.example.com"
        self.test_uri = "{}/volumes".format(self.test_url)
        self.test_token = "abc123"
        self.instantiate_args = (self.test_url, self.test_token)

        self.klass_name = "Volume"
        self.klass = getattr(Volume, self.klass_name)

    def test_class_exists(self):
        """
        Volume class is defined
        """

        self.assertTrue(hasattr(Volume, self.klass_name))

    def test_can_instantiate(self):
        """
        Volume class can be instantiated
        """

        exc_thrown = False

        try:
            self.klass(*self.instantiate_args)
        except Exception:
            exc_thrown = True

        self.assertFalse(exc_thrown)

    @patch('doboto.Volume.Volume.make_request')
    def test_list(self, mock_make_request):
        """
        list works
        """

        volume = self.klass(self.test_url, self.test_token)

        # Alone

        volume.list()
        mock_make_request.assert_called_with(self.test_uri)

        # By region

        region = "nyc1"
        volume.list(region)
        mock_make_request.assert_called_with(self.test_uri, params={"region": region})

    @patch('doboto.Volume.Volume.make_request')
    def test_create(self, mock_make_request):
        """
        create works with volume id
        """

        volume = self.klass(self.test_url, self.test_token)
        datas = {"name": "test.com", "region": "nyc3",
                 "size": "512mb", "image": "ubuntu-14-04-x64"}
        volume.create(datas)

        mock_make_request.assert_called_with(
            self.test_uri, 'POST', attribs=datas)

        # Check empty

        volume.create()

        mock_make_request.assert_called_with(
            self.test_uri, 'POST', attribs={})

    @patch('doboto.Volume.Volume.make_request')
    def test_info(self, mock_make_request):
        """
        info works with volume id or name
        """

        volume_id = 12345
        volume = self.klass(self.test_url, self.test_token)

        # By id

        volume.info(volume_id)
        test_uri = "{}/{}".format(self.test_uri, volume_id)
        mock_make_request.assert_called_with(test_uri)

        # By name

        volume.info(volume_name="stuff", region="nyc1")
        test_uri = self.test_uri
        mock_make_request.assert_called_with(test_uri, params={"name": "stuff", "region": "nyc1"})

        # Requirements met

        self.assertRaisesRegexp(
            ValueError, "Must supply an id or name and region", volume.info
        )
        self.assertRaisesRegexp(
            ValueError, "Must supply an id or name and region", volume.info, volume_name="stuff"
        )
        self.assertRaisesRegexp(
            ValueError, "Must supply an id or name and region", volume.info, region="nyc1"
        )

    @patch('doboto.Volume.Volume.make_request')
    def test_list_snapshots(self, mock_make_request):
        """
        list_snapshots works with volume id
        """

        volume_id = 12345
        volume = self.klass(self.test_url, self.test_token)
        volume.list_snapshots(volume_id)
        test_uri = "{}/{}/snapshots".format(self.test_uri, volume_id)

        mock_make_request.assert_called_with(test_uri)

    @patch('doboto.Volume.Volume.make_request')
    def test_take_snapshot(self, mock_make_request):
        """
        test take_snapshot works with volume id
        """
        volume = self.klass(self.test_url, self.test_token)
        volume_id = 12345
        test_uri = "{}/{}/snapshots".format(self.test_uri, volume_id)

        snap_name = "snap-1"
        datas = {"name": "%s" % (snap_name)}
        volume.take_snapshot(volume_id, snap_name)
        mock_make_request.assert_called_with(test_uri, 'POST', attribs=datas)

    @patch('doboto.Volume.Volume.make_request')
    def test_destroy(self, mock_make_request):
        """
        destroy works with volume id or name
        """

        volume_id = 12345
        volume = self.klass(self.test_url, self.test_token)

        # By id

        volume.destroy(volume_id)
        test_uri = "{}/{}".format(self.test_uri, volume_id)
        mock_make_request.assert_called_with(test_uri, "DELETE")

        # By name

        volume.destroy(volume_name="stuff", region="nyc1")
        test_uri = self.test_uri
        mock_make_request.assert_called_with(
            test_uri, "DELETE", params={"name": "stuff", "region": "nyc1"}
        )

        # Requirements met

        self.assertRaisesRegexp(
            ValueError, "Must supply an id or name and region", volume.destroy
        )
        self.assertRaisesRegexp(
            ValueError, "Must supply an id or name and region", volume.destroy, volume_name="stuff"
        )
        self.assertRaisesRegexp(
            ValueError, "Must supply an id or name and region", volume.destroy, region="nyc1"
        )

    @patch('doboto.Volume.Volume.make_request')
    def test_attach(self, mock_make_request):
        """
        test that attach works with volume_id and/or name
        """
        volume = self.klass(self.test_url, self.test_token)

        droplet_id = 123
        region = "nyc1"

        # By id

        volume_id = 12345
        test_uri = "{}/{}/actions".format(self.test_uri, volume_id)
        datas = {
            "type": "attach",
            "droplet_id": droplet_id,
            "region": region
        }
        volume.attach(droplet_id, region, volume_id)
        mock_make_request.assert_called_with(test_uri, 'POST', attribs=datas)

        # By name

        volume_name = "stuff"
        test_uri = "{}/actions".format(self.test_uri)
        datas = {
            "type": "attach",
            "droplet_id": droplet_id,
            "region": region,
            "volume_name": volume_name
        }
        volume.attach(droplet_id, region, volume_name=volume_name)
        mock_make_request.assert_called_with(test_uri, 'POST', attribs=datas)

        # Requirements met

        self.assertRaisesRegexp(
            ValueError, "Must supply an id or name", volume.attach, droplet_id, region
        )

    @patch('doboto.Volume.Volume.make_request')
    def test_detach(self, mock_make_request):
        """
        test that detach works with volume_id and/or name
        """
        volume = self.klass(self.test_url, self.test_token)

        droplet_id = 123
        region = "nyc1"

        # By id

        volume_id = 12345
        test_uri = "{}/{}/actions".format(self.test_uri, volume_id)
        datas = {
            "type": "detach",
            "droplet_id": droplet_id,
            "region": region
        }
        volume.detach(droplet_id, region, volume_id)
        mock_make_request.assert_called_with(test_uri, 'POST', attribs=datas)

        # By name

        volume_name = "stuff"
        test_uri = "{}/actions".format(self.test_uri)
        datas = {
            "type": "detach",
            "droplet_id": droplet_id,
            "region": region,
            "volume_name": volume_name
        }
        volume.detach(droplet_id, region, volume_name=volume_name)
        mock_make_request.assert_called_with(test_uri, 'POST', attribs=datas)

        # Requirements met

        self.assertRaisesRegexp(
            ValueError, "Must supply an id or name", volume.detach, droplet_id, region
        )

    @patch('doboto.Volume.Volume.make_request')
    def test_resize(self, mock_make_request):
        """
        test that resize works
        """
        volume = self.klass(self.test_url, self.test_token)

        volume_id = 12345
        region = "nyc1"
        size = 2
        test_uri = "{}/{}/actions".format(self.test_uri, volume_id)
        datas = {
            "type": "resize",
            "region": region,
            "size_gigabytes": 2
        }
        volume.resize(size, region, volume_id)
        mock_make_request.assert_called_with(test_uri, 'POST', attribs=datas)

    @patch('doboto.Volume.Volume.make_request')
    def test_list_actions(self, mock_make_request):
        """
        list_actions works with volume id
        """

        volume_id = 12345
        volume = self.klass(self.test_url, self.test_token)
        volume.list_actions(volume_id)
        test_uri = "{}/{}/actions".format(self.test_uri, volume_id)

        mock_make_request.assert_called_with(test_uri)

    @patch('doboto.Volume.Volume.make_request')
    def test_get_action(self, mock_make_request):
        """
        get_actions works with volume id and action id
        """

        volume_id = 12345
        action_id = 54321
        volume = self.klass(self.test_url, self.test_token)
        volume.get_action(volume_id, action_id)
        test_uri = "{}/{}/actions/{}".format(
            self.test_uri, volume_id, action_id)

        mock_make_request.assert_called_with(test_uri)
