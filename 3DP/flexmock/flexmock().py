from flexmock import flexmock

fake_plane = flexmock(
    model="MIG-16",
    condition="used")

print fake_plane, fake_plane.model