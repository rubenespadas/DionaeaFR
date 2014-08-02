from django import forms


class DownloadFilterForm(forms.Form):
    download_url = forms.CharField(
        label='Url',
        required=False
    )

    download_url.widget = forms.TextInput(
        attrs={
            'class': 'span10',
            'placeholder': 'Filter...'
        }
    )

    download_md5_hash = forms.CharField(
        label='MD5',
        required=False,
        max_length=32
    )

    download_md5_hash.widget = forms.TextInput(
        attrs={
            'class': 'span10',
            'placeholder': 'Filter...'
        }
    )

# vim: set expandtab:ts=4
