from django import forms

TRANSPORT = (
    ('', 'Select...'),
    ('tcp', 'tcp'),
    ('udp', 'udp'),
    ('tls', 'tls'),
)

STATE = (
    ('', 'Select...'),
    ('accept', 'accept'),
    ('connect', 'connect'),
    ('listen', 'listen'),
    ('reject', 'reject'),
)

PROTOCOL = (
    ('', 'Select...'),
    ('emulation', 'emulation'),
    ('epmapper', 'epmapper'),
    ('ftpctrl', 'ftpctrl'),
    ('ftpd', 'ftpd'),
    ('ftpdata', 'ftpdata'),
    ('ftpdataconnect', 'ftpdataconnect'),
    ('ftpdatalisten', 'ftpdatalisten'),
    ('httpd', 'httpd'),
    ('mirrorc', 'mirrorc'),
    ('mirrord', 'mirrord'),
    ('mssqld', 'mssqld'),
    ('mysqld', 'mysqld'),
    ('nc sink', 'nc sink'),
    ('pcap', 'pcap'),
    ('remoteshell', 'remoteshell'),
    ('RtpUdpStream', 'RtpUdpStream'),
    ('SipCall', 'SipCall'),
    ('SipSession', 'SipSession'),
    ('smbd', 'smbd'),
    ('TftpClient', 'TftpClient'),
    ('TftpServerHandler', 'TftpServerHandler'),
    ('xmppclient', 'xmppclient'),
)


class ConnectionFilterForm(forms.Form):
    connection_type = forms.CharField(
        label='State',
        required=False,
        max_length=255
    )

    connection_type.widget = forms.Select(
        attrs={
            'class': 'span10',
        },
        choices=STATE
    )

    connection_transport = forms.CharField(
        label='Transport',
        required=False,
        max_length=255
    )

    connection_transport.widget = forms.Select(
        attrs={
            'class': 'span10',
        },
        choices=TRANSPORT
    )

    connection_protocol = forms.CharField(
        label='Protocol',
        required=False,
        max_length=255
    )

    connection_protocol.widget = forms.Select(
        attrs={
            'class': 'span10',
        },
        choices=PROTOCOL
    )

    local_port = forms.IntegerField(
        label='Local Port',
        required=False
    )

    remote_host = forms.GenericIPAddressField(
        label='Attacker',
        required=False
    )

    remote_port = forms.IntegerField(
        label='Remote Port',
        required=False
    )

# vim: set expandtab:ts=4
