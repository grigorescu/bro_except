from django.db import models
import uuid

class Exemption(models.Model):
    """An exemption"""

    id_orig_h_net = models.ForeignKey("Subnet", null=True, blank=True, related_name="orig_h_net")
    id_resp_h_net = models.ForeignKey("Subnet", null=True, blank=True, related_name="resp_h_net")
    src_net = models.ForeignKey("Subnet", null=True, blank=True, related_name="src_net")
    dst_net = models.ForeignKey("Subnet", null=True, blank=True, related_name="dst_net")

    id_orig_p = models.ForeignKey("Port", null=True, blank=True, related_name="orig_p")
    id_resp_p = models.ForeignKey("Port", null=True, blank=True, related_name="resp_p")
    p = models.ForeignKey("Port", null=True, blank=True, related_name="p_p")

    note = models.ForeignKey("Note", null=True, blank=True)

    actor = models.CharField("Name of the person who put in the exemption", max_length=40)
    timestamp = models.DateTimeField(auto_now=True)


class Subnet(models.Model):
    """An IP subnet"""
    # id = models.unique_id
    base_ip = models.IPAddressField()
    cidr_range = models.IntegerField()

    def __str__(self):
        return "%s/%d" % (self.base_ip, self.cidr_range)


class Port(models.Model):
    """A network port"""
    port_num = models.IntegerField()

    PROTO_CHOICES = (
        ('T', "TCP"),
        ('U', "UDP"),
        ('I', "ICMP"),
    )

    proto = models.CharField(max_length=1, choices=PROTO_CHOICES)

    def to_proto(self, abbrev):
        if abbrev == "T": return 'tcp'
        if abbrev == "U": return 'udp'
        if abbrev == "I": return 'icmp'
        raise ValueError("Unknown protocol")

    def __str__(self):
        return "%s" % self.port_num


class Note(models.Model):
    """A type of notice, e.g. SSH::Password_Guessing"""

    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name


class Sensor(models.Model):
    """A Bro manager."""

    fqdn = models.CharField(max_length=50)
    api_key = models.CharField("API Key", max_length=70, editable=False)

    def __str__(self):
        return "%s" % self.fqdn

    def save(self):
        if not self.id:
            self.api_key = uuid.uuid4()
        super(Sensor, self).save()