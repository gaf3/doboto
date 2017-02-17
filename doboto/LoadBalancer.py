"""This holds the LoadBalancer class."""

import time
import copy
from .Endpoint import Endpoint
from .DOBOTOException import DOBOTOException



class LoadBalancer(Endpoint):

    """
    description:
        Load Balancers provide a way to distribute traffic across multiple Droplets. By sending
        requests to the /v2/load_balancers endpoint, you can list, create, or delete Load Balancers
        as well as add or remove Droplets, forwarding rules, and other configuration details.

    related: https://developers.digitalocean.com/documentation/v2/#load-balancers
    """

    def __init__(self, do, token, url, agent):
        """
        Takes token and agent and sets its DO for reference and URI for load_balancer interaction.
        """
        super(LoadBalancer, self).__init__(token, agent)
        self.do = do
        self.uri = "%s/load_balancers" % url
        self.reports = "%s/reports" % url

    def list(self):
        """
        description: List all Load Balancers

        out:
            A list of LoadBalancer dict's:
                - id - string - A unique ID that can be used to identify and reference a Load Balancer.
                - name - string - A human-readable name for a Load Balancer instance.
                - ip - string - An attribute containing the public-facing IP address of the Load Balancer.
                - algorithm - string - The load balancing algorithm used to determine which backend Droplet will be selected by a client. It must be either "round_robin" or "least_connections".
                - status - string - A status string indicating the current state of the Load Balancer. This can be "new", "active", or "errored".
                - created_at - string - A time value given in ISO8601 combined date and time format that represents when the Load Balancer was created.
                - forwarding_rules - list - Forwarding Roles dict's:
                    - entry_protocol - string - The protocol used for traffic to the Load Balancer. The possible values are: "http", "https", or "tcp".
                    - entry_port - int - An integer representing the port on which the Load Balancer instance will listen.
                    - target_protocol - string - The protocol used for traffic from the Load Balancer to the backend Droplets. The possible values are: "http", "https", or "tcp".
                    - target_port - int - An integer representing the port on the backend Droplets to which the Load Balancer will send traffic.
                    - certificate_id - string - The ID of the TLS certificate used for SSL termination if enabled.
                    - tls_passthrough - bool - A boolean value indicating whether SSL encrypted traffic will be passed through to the backend Droplets.
                - health_check - list - Health check dict's:
                    - protocol - string - The protocol used for health checks sent to the backend Droplets. The possible values are "http" or "tcp".
                    - port - int - An integer representing the port on the backend Droplets on which the health check will attempt a connection.
                    - path - string - The path on the backend Droplets to which the Load Balancer instance will send a request.
                    - check_interval_seconds - int - The number of seconds between between two consecutive health checks.
                    - response_timeout_seconds - int - The number of seconds the Load Balancer instance will wait for a response until marking a health check as failed.
                    - unhealthy_threshold - int - The number of times a health check must fail for a backend Droplet to be marked "unhealthy" and be removed from the pool.
                    - healthy_threshold - int - The number of times a health check must pass for a backend Droplet to be marked "healthy" and be re-added to the pool.
                - sticky_sessions - list - Sticky Session dict's:
                    - type - string - An attribute indicating how and if requests from a client will be persistently served by the same backend Droplet. The possible values are "cookies" or "none".
                    - cookie_name - string - The name of the cookie sent to the client. This attribute is only returned when using "cookies" for the sticky sessions type.
                    - cookie_ttl_seconds - string - The number of seconds until the cookie set by the Load Balancer expires. This attribute is only returned when using "cookies" for the sticky sessions type.
                - region - object - The region where the Load Balancer instance is located. When setting a region, the value should be the slug identifier for the region. When you query a Load Balancer, an entire region object will be returned.
                - tag - string - The name of a Droplet tag corresponding to Droplets assigned to the Load Balancer.
                - droplet_ids - array of integers - An array containing the IDs of the Droplets assigned to the Load Balancer.
                - redirect_http_to_https - bool - A boolean value indicating whether HTTP requests to the Load Balancer on port 80 will be redirected to HTTPS on port 443.

        related: https://developers.digitalocean.com/documentation/v2/#list-all-load_balancers

        """

        return self.pages(self.uri, "load_balancers")

    def create(self, attribs, wait=False, poll=5, timeout=300):
        """
        description: Create a new LoadBalancer

        in:
            - name - string - A human-readable name for a Load Balancer instance. - true
            - algorithm - string - The load balancing algorithm used to determine which backend Droplet will be selected by a client. It must be either "round_robin" or "least_connections". The default value is "round_robin". -
            - region - string - The region where the Load Balancer instance will be located. When setting a region, the value should be the slug identifier for the region. When you query a Load Balancer, an entire region object will be returned. - true
            - forwarding_rules - list - Forwarding Roles dict's:
                - entry_protocol - string - The protocol used for traffic to the Load Balancer. The possible values are: "http", "https", or "tcp".
                - entry_port - int - An integer representing the port on which the Load Balancer instance will listen.
                - target_protocol - string - The protocol used for traffic from the Load Balancer to the backend Droplets. The possible values are: "http", "https", or "tcp".
                - target_port - int - An integer representing the port on the backend Droplets to which the Load Balancer will send traffic.
                - certificate_id - string - The ID of the TLS certificate used for SSL termination if enabled.
                - tls_passthrough - bool - A boolean value indicating whether SSL encrypted traffic will be passed through to the backend Droplets.
            - health_check - list - Health check dict's:
                - protocol - string - The protocol used for health checks sent to the backend Droplets. The possible values are "http" or "tcp".
                - port - int - An integer representing the port on the backend Droplets on which the health check will attempt a connection.
                - path - string - The path on the backend Droplets to which the Load Balancer instance will send a request.
                - check_interval_seconds - int - The number of seconds between between two consecutive health checks.
                - response_timeout_seconds - int - The number of seconds the Load Balancer instance will wait for a response until marking a health check as failed.
                - unhealthy_threshold - int - The number of times a health check must fail for a backend Droplet to be marked "unhealthy" and be removed from the pool.
                - healthy_threshold - int - The number of times a health check must pass for a backend Droplet to be marked "healthy" and be re-added to the pool.
            - sticky_sessions - list - Sticky Session dict's:
                - type - string - An attribute indicating how and if requests from a client will be persistently served by the same backend Droplet. The possible values are "cookies" or "none".
                - cookie_name - string - The name of the cookie sent to the client. This attribute is only returned when using "cookies" for the sticky sessions type.
                - cookie_ttl_seconds - string - The number of seconds until the cookie set by the Load Balancer expires. This attribute is only returned when using "cookies" for the sticky sessions type.
            - redirect_http_to_https - bool - A boolean value indicating whether HTTP requests to the Load Balancer on port 80 will be redirected to HTTPS on port 443. Default value is false. -
            - droplet_ids - array of integers - An array containing the IDs of the Droplets to be assigned to the Load Balancer.
            - tag - string - The name of a Droplet tag corresponding to Droplets to be assigned to the Load Balancer.

        out:
            A LoadBalancer dict:
                - id - string - A unique ID that can be used to identify and reference a Load Balancer.
                - name - string - A human-readable name for a Load Balancer instance.
                - ip - string - An attribute containing the public-facing IP address of the Load Balancer.
                - algorithm - string - The load balancing algorithm used to determine which backend Droplet will be selected by a client. It must be either "round_robin" or "least_connections".
                - status - string - A status string indicating the current state of the Load Balancer. This can be "new", "active", or "errored".
                - created_at - string - A time value given in ISO8601 combined date and time format that represents when the Load Balancer was created.
                - forwarding_rules - list - Forwarding Roles dict's:
                    - entry_protocol - string - The protocol used for traffic to the Load Balancer. The possible values are: "http", "https", or "tcp".
                    - entry_port - int - An integer representing the port on which the Load Balancer instance will listen.
                    - target_protocol - string - The protocol used for traffic from the Load Balancer to the backend Droplets. The possible values are: "http", "https", or "tcp".
                    - target_port - int - An integer representing the port on the backend Droplets to which the Load Balancer will send traffic.
                    - certificate_id - string - The ID of the TLS certificate used for SSL termination if enabled.
                    - tls_passthrough - bool - A boolean value indicating whether SSL encrypted traffic will be passed through to the backend Droplets.
                - health_check - list - Health check dict's:
                    - protocol - string - The protocol used for health checks sent to the backend Droplets. The possible values are "http" or "tcp".
                    - port - int - An integer representing the port on the backend Droplets on which the health check will attempt a connection.
                    - path - string - The path on the backend Droplets to which the Load Balancer instance will send a request.
                    - check_interval_seconds - int - The number of seconds between between two consecutive health checks.
                    - response_timeout_seconds - int - The number of seconds the Load Balancer instance will wait for a response until marking a health check as failed.
                    - unhealthy_threshold - int - The number of times a health check must fail for a backend Droplet to be marked "unhealthy" and be removed from the pool.
                    - healthy_threshold - int - The number of times a health check must pass for a backend Droplet to be marked "healthy" and be re-added to the pool.
                - sticky_sessions - list - Sticky Session dict's:
                    - type - string - An attribute indicating how and if requests from a client will be persistently served by the same backend Droplet. The possible values are "cookies" or "none".
                    - cookie_name - string - The name of the cookie sent to the client. This attribute is only returned when using "cookies" for the sticky sessions type.
                    - cookie_ttl_seconds - string - The number of seconds until the cookie set by the Load Balancer expires. This attribute is only returned when using "cookies" for the sticky sessions type.
                - region - object - The region where the Load Balancer instance is located. When setting a region, the value should be the slug identifier for the region. When you query a Load Balancer, an entire region object will be returned.
                - tag - string - The name of a Droplet tag corresponding to Droplets assigned to the Load Balancer.
                - droplet_ids - array of integers - An array containing the IDs of the Droplets assigned to the Load Balancer.
                - redirect_http_to_https - bool - A boolean value indicating whether HTTP requests to the Load Balancer on port 80 will be redirected to HTTPS on port 443.

        related:
            - https://developers.digitalocean.com/documentation/v2/#create-a-new-load_balancers
            - https://developers.digitalocean.com/documentation/v2/#create-a-new-load-balancer-with-droplet-tag
        """

        load_balancer = self.request(self.uri, "load_balancer", 'POST', attribs=attribs)

        start_time = time.time()

        while wait and not self.ready(load_balancer, attribs):

            time.sleep(poll)
            try:
                droplet = self.info(load_balancer["id"])
            except:
                pass

            if time.time() - start_time > timeout:
                raise DOBOTOException("Timeout on polling", load_balancer)

        return load_balancer

    def present(self, attribs, wait=False, poll=5, timeout=300):
        """
        description: Create a new LoadBalancer if not already existing

        in:
            - name - string - A human-readable name for a Load Balancer instance. - true
            - algorithm - string - The load balancing algorithm used to determine which backend Droplet will be selected by a client. It must be either "round_robin" or "least_connections". The default value is "round_robin". -
            - region - string - The region where the Load Balancer instance will be located. When setting a region, the value should be the slug identifier for the region. When you query a Load Balancer, an entire region object will be returned. - true
            - forwarding_rules - list - Forwarding Roles dict's:
                - entry_protocol - string - The protocol used for traffic to the Load Balancer. The possible values are: "http", "https", or "tcp".
                - entry_port - int - An integer representing the port on which the Load Balancer instance will listen.
                - target_protocol - string - The protocol used for traffic from the Load Balancer to the backend Droplets. The possible values are: "http", "https", or "tcp".
                - target_port - int - An integer representing the port on the backend Droplets to which the Load Balancer will send traffic.
                - certificate_id - string - The ID of the TLS certificate used for SSL termination if enabled.
                - tls_passthrough - bool - A boolean value indicating whether SSL encrypted traffic will be passed through to the backend Droplets.
            - health_check - list - Health check dict's:
                - protocol - string - The protocol used for health checks sent to the backend Droplets. The possible values are "http" or "tcp".
                - port - int - An integer representing the port on the backend Droplets on which the health check will attempt a connection.
                - path - string - The path on the backend Droplets to which the Load Balancer instance will send a request.
                - check_interval_seconds - int - The number of seconds between between two consecutive health checks.
                - response_timeout_seconds - int - The number of seconds the Load Balancer instance will wait for a response until marking a health check as failed.
                - unhealthy_threshold - int - The number of times a health check must fail for a backend Droplet to be marked "unhealthy" and be removed from the pool.
                - healthy_threshold - int - The number of times a health check must pass for a backend Droplet to be marked "healthy" and be re-added to the pool.
            - sticky_sessions - list - Sticky Session dict's:
                - type - string - An attribute indicating how and if requests from a client will be persistently served by the same backend Droplet. The possible values are "cookies" or "none".
                - cookie_name - string - The name of the cookie sent to the client. This attribute is only returned when using "cookies" for the sticky sessions type.
                - cookie_ttl_seconds - string - The number of seconds until the cookie set by the Load Balancer expires. This attribute is only returned when using "cookies" for the sticky sessions type.
            - redirect_http_to_https - bool - A boolean value indicating whether HTTP requests to the Load Balancer on port 80 will be redirected to HTTPS on port 443. Default value is false. -
            - droplet_ids - array of integers - An array containing the IDs of the Droplets to be assigned to the Load Balancer.
            - tag - string - The name of a Droplet tag corresponding to Droplets to be assigned to the Load Balancer.

        out:
            A tuple of two Load Balancer dict's (second is None if already present):
                - id - string - A unique ID that can be used to identify and reference a Load Balancer.
                - name - string - A human-readable name for a Load Balancer instance.
                - ip - string - An attribute containing the public-facing IP address of the Load Balancer.
                - algorithm - string - The load balancing algorithm used to determine which backend Droplet will be selected by a client. It must be either "round_robin" or "least_connections".
                - status - string - A status string indicating the current state of the Load Balancer. This can be "new", "active", or "errored".
                - created_at - string - A time value given in ISO8601 combined date and time format that represents when the Load Balancer was created.
                - forwarding_rules - list - Forwarding Roles dict's:
                    - entry_protocol - string - The protocol used for traffic to the Load Balancer. The possible values are: "http", "https", or "tcp".
                    - entry_port - int - An integer representing the port on which the Load Balancer instance will listen.
                    - target_protocol - string - The protocol used for traffic from the Load Balancer to the backend Droplets. The possible values are: "http", "https", or "tcp".
                    - target_port - int - An integer representing the port on the backend Droplets to which the Load Balancer will send traffic.
                    - certificate_id - string - The ID of the TLS certificate used for SSL termination if enabled.
                    - tls_passthrough - bool - A boolean value indicating whether SSL encrypted traffic will be passed through to the backend Droplets.
                - health_check - list - Health check dict's:
                    - protocol - string - The protocol used for health checks sent to the backend Droplets. The possible values are "http" or "tcp".
                    - port - int - An integer representing the port on the backend Droplets on which the health check will attempt a connection.
                    - path - string - The path on the backend Droplets to which the Load Balancer instance will send a request.
                    - check_interval_seconds - int - The number of seconds between between two consecutive health checks.
                    - response_timeout_seconds - int - The number of seconds the Load Balancer instance will wait for a response until marking a health check as failed.
                    - unhealthy_threshold - int - The number of times a health check must fail for a backend Droplet to be marked "unhealthy" and be removed from the pool.
                    - healthy_threshold - int - The number of times a health check must pass for a backend Droplet to be marked "healthy" and be re-added to the pool.
                - sticky_sessions - list - Sticky Session dict's:
                    - type - string - An attribute indicating how and if requests from a client will be persistently served by the same backend Droplet. The possible values are "cookies" or "none".
                    - cookie_name - string - The name of the cookie sent to the client. This attribute is only returned when using "cookies" for the sticky sessions type.
                    - cookie_ttl_seconds - string - The number of seconds until the cookie set by the Load Balancer expires. This attribute is only returned when using "cookies" for the sticky sessions type.
                - region - object - The region where the Load Balancer instance is located. When setting a region, the value should be the slug identifier for the region. When you query a Load Balancer, an entire region object will be returned.
                - tag - string - The name of a Droplet tag corresponding to Droplets assigned to the Load Balancer.
                - droplet_ids - array of integers - An array containing the IDs of the Droplets assigned to the Load Balancer.
                - redirect_http_to_https - bool - A boolean value indicating whether HTTP requests to the Load Balancer on port 80 will be redirected to HTTPS on port 443.
        """

        load_balancers = self.list()

        if "name" in attribs:

            existing = None
            for load_balancer in load_balancers:
                if attrib["name"] == load_balancer["name"]:
                    existing = load_balancer
                    break

            if existing is not None:
                return (existing, None)

            created = self.create(name, private_key, leaf_load_balancer, load_balancer_chain)
            return (created, created)

        else:

            raise ValueError("name must be specified")

    def info(self, id):
        """
        description: Retrieve an existing LoadBalancer by id

        in:
            - id - number - The id of the LoadBalancer to retrieve

        out:
            A LoadBalancer dict:
                - id - string - A unique ID that can be used to identify and reference a Load Balancer.
                - name - string - A human-readable name for a Load Balancer instance.
                - ip - string - An attribute containing the public-facing IP address of the Load Balancer.
                - algorithm - string - The load balancing algorithm used to determine which backend Droplet will be selected by a client. It must be either "round_robin" or "least_connections".
                - status - string - A status string indicating the current state of the Load Balancer. This can be "new", "active", or "errored".
                - created_at - string - A time value given in ISO8601 combined date and time format that represents when the Load Balancer was created.
                - forwarding_rules - list - Forwarding Roles dict's:
                    - entry_protocol - string - The protocol used for traffic to the Load Balancer. The possible values are: "http", "https", or "tcp".
                    - entry_port - int - An integer representing the port on which the Load Balancer instance will listen.
                    - target_protocol - string - The protocol used for traffic from the Load Balancer to the backend Droplets. The possible values are: "http", "https", or "tcp".
                    - target_port - int - An integer representing the port on the backend Droplets to which the Load Balancer will send traffic.
                    - certificate_id - string - The ID of the TLS certificate used for SSL termination if enabled.
                    - tls_passthrough - bool - A boolean value indicating whether SSL encrypted traffic will be passed through to the backend Droplets.
                - health_check - list - Health check dict's:
                    - protocol - string - The protocol used for health checks sent to the backend Droplets. The possible values are "http" or "tcp".
                    - port - int - An integer representing the port on the backend Droplets on which the health check will attempt a connection.
                    - path - string - The path on the backend Droplets to which the Load Balancer instance will send a request.
                    - check_interval_seconds - int - The number of seconds between between two consecutive health checks.
                    - response_timeout_seconds - int - The number of seconds the Load Balancer instance will wait for a response until marking a health check as failed.
                    - unhealthy_threshold - int - The number of times a health check must fail for a backend Droplet to be marked "unhealthy" and be removed from the pool.
                    - healthy_threshold - int - The number of times a health check must pass for a backend Droplet to be marked "healthy" and be re-added to the pool.
                - sticky_sessions - list - Sticky Session dict's:
                    - type - string - An attribute indicating how and if requests from a client will be persistently served by the same backend Droplet. The possible values are "cookies" or "none".
                    - cookie_name - string - The name of the cookie sent to the client. This attribute is only returned when using "cookies" for the sticky sessions type.
                    - cookie_ttl_seconds - string - The number of seconds until the cookie set by the Load Balancer expires. This attribute is only returned when using "cookies" for the sticky sessions type.
                - region - object - The region where the Load Balancer instance is located. When setting a region, the value should be the slug identifier for the region. When you query a Load Balancer, an entire region object will be returned.
                - tag - string - The name of a Droplet tag corresponding to Droplets assigned to the Load Balancer.
                - droplet_ids - array of integers - An array containing the IDs of the Droplets assigned to the Load Balancer.
                - redirect_http_to_https - bool - A boolean value indicating whether HTTP requests to the Load Balancer on port 80 will be redirected to HTTPS on port 443.

        related: https://developers.digitalocean.com/documentation/v2/#retrieve-an-existing-load_balancers
        """

        return self.request("%s/%s" % (self.uri, id), "load_balancer")

    def destroy(self, id):
        """
        description: Delete a LoadBalancer

        in:
            - id - number - The id of the LoadBalancer to destroy

        out: None. A DOBOTOException is thrown if an issue is encountered.

        related: https://developers.digitalocean.com/documentation/v2/#delete-a-load_balancers
        """

        return self.request("%s/%s" % (self.uri, id), request_method='DELETE')
