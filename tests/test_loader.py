#!/usr/bin/env python

#
# Copyright (c) 2013, Digium, Inc.
#

import unittest
import swaggerpy

from swaggerpy import swagger_model


class TestProcessor(swagger_model.SwaggerProcessor):
    def process_resource_listing(self, resources, context):
        resources['processed'] = True


class TestProcessorTestCase(unittest.TestCase):

    def test_process_resource_listing(self):
        # Given: An instance of TestProcessor
        processor = TestProcessor()

        # And: A sample resources dictionary
        resources = {}
        context = None  # or whatever context you want to provide

        # When: The process_resource_listing method is called
        processor.process_resource_listing(resources, context)

        # Then: The resources dictionary should have the key 'processed' set to True
        self.assertTrue(resources.get('processed'))

class LoaderTest(unittest.TestCase):
    def test_simple(self):
        uut = swaggerpy.load_file('test-data/1.1/simple/resources.json')
        self.assertEqual('1.1', uut['swaggerVersion'])
        decl = uut['apis'][0]['api_declaration']
        self.assertEqual(1, len(decl['models']))
        self.assertEqual(1, len(decl['models']['Simple']['properties']))

    def test_processor(self):
        uut = swaggerpy.load_file('test-data/1.1/simple/resources.json',
                                  processors=[TestProcessor()])
        self.assertEqual('1.1', uut['swaggerVersion'])
        self.assertTrue(uut['processed'])

    def test_missing(self):
        try:
            swaggerpy.load_file(
                'test-data/1.1/missing_resource/resources.json')
            self.fail("Expected load failure b/c of missing file")
        except IOError:
            pass


if __name__ == '__main__':
    unittest.main()
