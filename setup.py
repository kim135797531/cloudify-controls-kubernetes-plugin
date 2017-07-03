from setuptools import setup

# Replace the place holders with values for your project

setup(

    # Do not use underscores in the plugin name.
    name='ENTER-PLUGIN-NAME-HERE',

    version='0.1',
    author='ENTER-AUTHOR-HERE',
    author_email='ENTER-AUTHOR-EMAIL-HERE',
    description='ENTER-DESCRIPTION-HERE',

    # This must correspond to the actual packages in the plugin.
    packages=['plugin'],

    license='LICENSE',
    zip_safe=False,
    install_requires=[
        # Necessary dependency for developing plugins, do not remove!
        "cloudify-plugins-common>=4.0"
    ],
    test_requires=[
        "cloudify-dsl-parser>=4.0"
        "nose"
    ]
)