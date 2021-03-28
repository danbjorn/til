---
created: 2021-01-19
tag: django
title: Django FileField without a form
---
You can use the `FileField` model field type in Django without binding it to a form.
You can use the `File` object to wrap your desired file with a name and pass it as the
field’s value. When you call `save()` it will copy it to the storage. If you use a
`TemporaryUploadedFile` it will move the file rather than copy it.

Alternatively you can use the storage engine directly. `default_storage` is a shortcut
to whatever the configured default engine is, normally the one backed by `MEDIA_ROOT`.
The engine has a number of useful methods to manipulate the storage.

Note: don’t do what I did and mock `MEDIA_URL` instead of `MEDIA_ROOT` in the tests.
You will get very confused.

