#!/usr/bin/env python

import httplib;
import json;

class Analytics():

    def __init__(self, domain):
        self.domain = domain;
        self.service = 'heroku-buildpack-typekit';
        self.endpoint = 'jedkirby-develop-pr-51.herokuapp.com';

    ##
    # Create a secure connection.
    #
    # @return HTTPSConnection
    ##
    def connection(self):
        return httplib.HTTPSConnection(self.endpoint);

    ##
    # Using the connection, make a request to the API using the correct endpoint.
    #
    # @param string method
    # @param string endpoint
    # @param string body
    #
    # @return bool|object
    ##
    def request(self, method, endpoint, body = ''):
        try :
            conn = self.connection();
            conn.request(method, endpoint, body, {});
            response = conn.getresponse();
            if response.status != 200:
                return False;
            else:
                return json.loads(
                    response.read()
                );
        finally:
            conn.close();

    ##
    # Compile a list of params for the ping to register with the correct application.
    #
    # @return string
    ##
    def params(self):
        return ','.join([
            'domain=' + self.domain,
            'service=' + self.service
        ]);

    ##
    # Ping the usage of the buildback purely
    # for statistical information.
    #
    # @return bool
    ##
    def ping(self):
        response = self.request('POST', '/api/v1/ping', self.params());
        return True if response else False;
