import subprocess
import uuid

import pytest
import testinfra


@pytest.fixture(scope="class")
def host(request):
    random_uuid = uuid.uuid4()
    image_name = f"kafka-testbed-prometheus-ecs-{random_uuid}"

    subprocess.check_call(["docker", "build", "-t", image_name, "."])

    docker_id = (
        subprocess.check_output(
            ["docker", "run", "--entrypoint", "/bin/sh", "-i", "-t", "-d", image_name]
        )
        .decode()
        .strip()
    )

    host = testinfra.get_host("docker://" + docker_id)
    request.cls.host = host
    yield host

    subprocess.check_call(["docker", "rm", "-f", docker_id])
