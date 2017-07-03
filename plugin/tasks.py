# ctx is imported and used in operations
from cloudify import ctx

# put the operation decorator on any function that is a task
from cloudify.decorators import operation


@operation
def my_task(some_property, **kwargs):
    # setting node instance runtime property
    ctx.instance.runtime_properties['some_property'] = some_property
