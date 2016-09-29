import botocore.session
from botocore.utils import fix_s3_host

__all__ = ['get_session']

# We cache two sessions
# So we have one session with the s3 host-subdomain hook for AWS connections
# and one without the hook for custom endpoints
sessions = [None, None]

def get_session(endpoint=None):
    session = sessions[bool(endpoint)]
    if session is None:
        session = sessions[bool(endpoint)] = botocore.session.get_session()
        if endpoint:
            session.unregister('before-sign.s3', fix_s3_host)
    return session
