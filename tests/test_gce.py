from __future__ import print_function
import pytest

__TEST_INSTANCE__ = "gcpm-test-instance"


@pytest.mark.compute
def test_zones(default_gcpm):
    zones = default_gcpm.get_gce().get_zones()
    print(zones)
    assert "asia-northeast1-b" in zones


# option={"machineType": "custom-2-5120"}
# option={"machineType": "n1-standard-1"}
@pytest.mark.compute
def test_create(default_gcpm):
    assert default_gcpm.get_gce().create_instance(
        instance=__TEST_INSTANCE__,
        option={
            "machineType": "custom-2-5120",
            "family": "centos-7",
            "project": "centos-cloud",
        }
    )


@pytest.mark.parametrize(
    "instance_filter", [{}, {"status": "RUNNING"}])
@pytest.mark.compute
def test_instances(default_gcpm, instance_filter):
    instances = default_gcpm.get_gce().get_instances(
        update=True, instance_filter=instance_filter)
    assert __TEST_INSTANCE__ in instances


@pytest.mark.compute
def test_stop(default_gcpm):
    assert default_gcpm.get_gce().stop_instance(__TEST_INSTANCE__)


@pytest.mark.compute
def test_instances_terminated(default_gcpm):
    instances = default_gcpm.get_gce().get_instances(
        update=True, instance_filter={"status": "TERMINATED"})
    assert __TEST_INSTANCE__ in instances


@pytest.mark.compute
def test_start(default_gcpm):
    assert default_gcpm.get_gce().start_instance(__TEST_INSTANCE__)


@pytest.mark.compute
def test_delete(default_gcpm):
    assert default_gcpm.get_gce().delete_instance(__TEST_INSTANCE__)


@pytest.mark.compute
def test_instances_deleted(default_gcpm):
    instances = default_gcpm.get_gce().get_instances(
        update=True, instance_filter={})
    print(instances)
    assert __TEST_INSTANCE__ not in instances
