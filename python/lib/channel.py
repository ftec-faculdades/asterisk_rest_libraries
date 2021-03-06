"""
 Copyright (C) 2013 Digium, Inc.

 Erin Spiceland <espiceland@digium.com>

 See http://www.asterisk.org for more information about
 the Asterisk project. Please do not directly contact
 any of the maintainers of this project for assistance;
 the project provides a web site, mailing lists and IRC
 channels for your use.

 This program is free software, distributed under the terms
 detailed in the the LICENSE file at the top of the source tree.

"""


class Channel:
    """Definition of Channel object."""
    def __init__(self, api):
        """Initialize the Channel object."""
        self.object_id = 1
        self._api = api

    def get_id(self):
        """Return the Channel object's id."""
        return self.object_id

    def add_event_handler(self, event_name, handler):
        """Add an event handler for Stasis events on this object.
        For general events, use Asterisk.add_event_handler instead.
        """
        pass

    def remove_event_handler(self, event_name, handler):
        """Remove an event handler for Stasis events on this object.
        For general events, use Asterisk.remove_event_handler instead.
        """
        pass

    def originate(self, endpoint_string=None, extension_string=None,
                  context_string=None):
        """Active channels; Create a new channel (originate)"""
        params = {}
        if endpoint_string:
            params['endpoint'] = endpoint_string
        if extension_string:
            params['extension'] = extension_string
        if context_string:
            params['context'] = context_string

        self._api.call('/channels', http_method='POST', parameters=params)
        is_success = True
        return is_success

    def delete(self):
        """Active channel; Delete (i.e. hangup) a channel"""
        params = {}

        self._api.call('/channels/%s', http_method='DELETE', parameters=params,
                       object_id=self.object_id)
        is_success = True
        return is_success

    def dial(self, endpoint_string=None, extension_string=None,
             context_string=None):
        """Create a new channel (originate) and bridge to this channel"""
        params = {}
        if endpoint_string:
            params['endpoint'] = endpoint_string
        if extension_string:
            params['extension'] = extension_string
        if context_string:
            params['context'] = context_string

        self._api.call('/channels/%s/dial', http_method='POST',
                       parameters=params, object_id=self.object_id)
        is_success = True
        return is_success

    def continue_in_dialplan(self):
        """Exit application; continue execution in the dialplan"""
        params = {}

        self._api.call('/channels/%s/continue', http_method='POST',
                       parameters=params, object_id=self.object_id)
        is_success = True
        return is_success

    def reject(self):
        """Reject a channel"""
        params = {}

        self._api.call('/channels/%s/reject', http_method='POST',
                       parameters=params, object_id=self.object_id)
        is_success = True
        return is_success

    def answer(self):
        """Answer a channel"""
        params = {}

        self._api.call('/channels/%s/answer', http_method='POST',
                       parameters=params, object_id=self.object_id)
        is_success = True
        return is_success

    def mute(self, direction_string='both'):
        """Mute a channel"""
        params = {}
        if direction_string:
            params['direction'] = direction_string

        self._api.call('/channels/%s/mute', http_method='POST',
                       parameters=params, object_id=self.object_id)
        is_success = True
        return is_success

    def unmute(self, direction_string='both'):
        """Unmute a channel"""
        params = {}
        if direction_string:
            params['direction'] = direction_string

        self._api.call('/channels/%s/unmute', http_method='POST',
                       parameters=params, object_id=self.object_id)
        is_success = True
        return is_success

    def record(self, name_string=None, max_duration_seconds_int='0',
               max_silence_seconds_int='0', append_boolean='False',
               beep_boolean='False', terminate_on_string='none'):
        """Record audio to/from a channel; Start a recording"""
        params = {}
        if name_string:
            params['name'] = name_string
        if max_duration_seconds_int:
            params['maxDurationSeconds'] = max_duration_seconds_int
        if max_silence_seconds_int:
            params['maxSilenceSeconds'] = max_silence_seconds_int
        if append_boolean:
            params['append'] = append_boolean
        if beep_boolean:
            params['beep'] = beep_boolean
        if terminate_on_string:
            params['terminateOn'] = terminate_on_string

        self._api.call('/channels/%s/record', http_method='POST',
                       parameters=params, object_id=self.object_id)
        is_success = True
        return is_success
