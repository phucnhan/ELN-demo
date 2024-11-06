# Generated by Django 3.2.23 on 2024-01-25 21:56

from django.db import migrations

from lms.djangoapps.certificates.data import CertificateStatuses


class Migration(migrations.Migration):
    """
    If any certificates exist with an invalidation record that are not marked as unavailable,
    change their status. Irreversible.
    """

    dependencies = [
        ("certificates", "0036_modifiedcertificatetemplatecommandconfiguration"),
    ]

    def make_invalid_certificates_unavailable(apps, schema_editor):
        GeneratedCertificate = apps.get_model("certificates", "GeneratedCertificate")

        GeneratedCertificate.objects.filter(
            certificateinvalidation__active=True
        ).exclude(status=CertificateStatuses.unavailable).update(
            status=CertificateStatuses.unavailable
        )

    operations = [
        migrations.RunPython(
            make_invalid_certificates_unavailable,
            reverse_code=migrations.RunPython.noop,
        )
    ]