# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import unittest2


class TestRow(unittest2.TestCase):

    def _getTargetClass(self):
        from gcloud.bigtable.row import Row
        return Row

    def _makeOne(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def test_constructor(self):
        row_key = b'row_key'
        table = object()

        row = self._makeOne(row_key, table)
        self.assertEqual(row._row_key, row_key)
        self.assertTrue(row._table is table)

    def test_constructor_with_unicode(self):
        row_key = u'row_key'
        row_key_bytes = b'row_key'
        table = object()

        row = self._makeOne(row_key, table)
        self.assertEqual(row._row_key, row_key_bytes)
        self.assertTrue(row._table is table)

    def test_constructor_with_non_bytes(self):
        row_key = object()
        with self.assertRaises(TypeError):
            self._makeOne(row_key, None)


class Test_BoolFilter(unittest2.TestCase):

    def _getTargetClass(self):
        from gcloud.bigtable.row import _BoolFilter
        return _BoolFilter

    def _makeOne(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def test_constructor(self):
        flag = object()
        row_filter = self._makeOne(flag)
        self.assertTrue(row_filter.flag is flag)

    def test___eq__type_differ(self):
        flag = object()
        row_filter1 = self._makeOne(flag)
        row_filter2 = object()
        self.assertNotEqual(row_filter1, row_filter2)

    def test___eq__same_value(self):
        flag = object()
        row_filter1 = self._makeOne(flag)
        row_filter2 = self._makeOne(flag)
        self.assertEqual(row_filter1, row_filter2)

    def test___ne__same_value(self):
        flag = object()
        row_filter1 = self._makeOne(flag)
        row_filter2 = self._makeOne(flag)
        comparison_val = (row_filter1 != row_filter2)
        self.assertFalse(comparison_val)


class TestSinkFilter(unittest2.TestCase):

    def _getTargetClass(self):
        from gcloud.bigtable.row import SinkFilter
        return SinkFilter

    def _makeOne(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def test_to_pb(self):
        from gcloud.bigtable._generated import bigtable_data_pb2 as data_pb2

        flag = True
        row_filter = self._makeOne(flag)
        pb_val = row_filter.to_pb()
        expected_pb = data_pb2.RowFilter(sink=flag)
        self.assertEqual(pb_val, expected_pb)


class TestPassAllFilter(unittest2.TestCase):

    def _getTargetClass(self):
        from gcloud.bigtable.row import PassAllFilter
        return PassAllFilter

    def _makeOne(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def test_to_pb(self):
        from gcloud.bigtable._generated import bigtable_data_pb2 as data_pb2

        flag = True
        row_filter = self._makeOne(flag)
        pb_val = row_filter.to_pb()
        expected_pb = data_pb2.RowFilter(pass_all_filter=flag)
        self.assertEqual(pb_val, expected_pb)


class TestBlockAllFilter(unittest2.TestCase):

    def _getTargetClass(self):
        from gcloud.bigtable.row import BlockAllFilter
        return BlockAllFilter

    def _makeOne(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def test_to_pb(self):
        from gcloud.bigtable._generated import bigtable_data_pb2 as data_pb2

        flag = True
        row_filter = self._makeOne(flag)
        pb_val = row_filter.to_pb()
        expected_pb = data_pb2.RowFilter(block_all_filter=flag)
        self.assertEqual(pb_val, expected_pb)


class Test_RegexFilter(unittest2.TestCase):

    def _getTargetClass(self):
        from gcloud.bigtable.row import _RegexFilter
        return _RegexFilter

    def _makeOne(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def test_constructor(self):
        regex = object()
        row_filter = self._makeOne(regex)
        self.assertTrue(row_filter.regex is regex)

    def test___eq__type_differ(self):
        regex = object()
        row_filter1 = self._makeOne(regex)
        row_filter2 = object()
        self.assertNotEqual(row_filter1, row_filter2)

    def test___eq__same_value(self):
        regex = object()
        row_filter1 = self._makeOne(regex)
        row_filter2 = self._makeOne(regex)
        self.assertEqual(row_filter1, row_filter2)

    def test___ne__same_value(self):
        regex = object()
        row_filter1 = self._makeOne(regex)
        row_filter2 = self._makeOne(regex)
        comparison_val = (row_filter1 != row_filter2)
        self.assertFalse(comparison_val)


class TestRowKeyRegexFilter(unittest2.TestCase):

    def _getTargetClass(self):
        from gcloud.bigtable.row import RowKeyRegexFilter
        return RowKeyRegexFilter

    def _makeOne(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def test_to_pb(self):
        from gcloud.bigtable._generated import bigtable_data_pb2 as data_pb2

        regex = b'row-key-regex'
        row_filter = self._makeOne(regex)
        pb_val = row_filter.to_pb()
        expected_pb = data_pb2.RowFilter(row_key_regex_filter=regex)
        self.assertEqual(pb_val, expected_pb)


class TestRowSampleFilter(unittest2.TestCase):

    def _getTargetClass(self):
        from gcloud.bigtable.row import RowSampleFilter
        return RowSampleFilter

    def _makeOne(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def test_constructor(self):
        sample = object()
        row_filter = self._makeOne(sample)
        self.assertTrue(row_filter.sample is sample)

    def test___eq__type_differ(self):
        sample = object()
        row_filter1 = self._makeOne(sample)
        row_filter2 = object()
        self.assertNotEqual(row_filter1, row_filter2)

    def test___eq__same_value(self):
        sample = object()
        row_filter1 = self._makeOne(sample)
        row_filter2 = self._makeOne(sample)
        self.assertEqual(row_filter1, row_filter2)

    def test_to_pb(self):
        from gcloud.bigtable._generated import bigtable_data_pb2 as data_pb2

        sample = 0.25
        row_filter = self._makeOne(sample)
        pb_val = row_filter.to_pb()
        expected_pb = data_pb2.RowFilter(row_sample_filter=sample)
        self.assertEqual(pb_val, expected_pb)


class TestFamilyNameRegexFilter(unittest2.TestCase):

    def _getTargetClass(self):
        from gcloud.bigtable.row import FamilyNameRegexFilter
        return FamilyNameRegexFilter

    def _makeOne(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def test_to_pb(self):
        from gcloud.bigtable._generated import bigtable_data_pb2 as data_pb2

        regex = u'family-regex'
        row_filter = self._makeOne(regex)
        pb_val = row_filter.to_pb()
        expected_pb = data_pb2.RowFilter(family_name_regex_filter=regex)
        self.assertEqual(pb_val, expected_pb)


class TestColumnQualifierRegexFilter(unittest2.TestCase):

    def _getTargetClass(self):
        from gcloud.bigtable.row import ColumnQualifierRegexFilter
        return ColumnQualifierRegexFilter

    def _makeOne(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def test_to_pb(self):
        from gcloud.bigtable._generated import bigtable_data_pb2 as data_pb2

        regex = b'column-regex'
        row_filter = self._makeOne(regex)
        pb_val = row_filter.to_pb()
        expected_pb = data_pb2.RowFilter(column_qualifier_regex_filter=regex)
        self.assertEqual(pb_val, expected_pb)


class TestColumnRangeFilter(unittest2.TestCase):

    def _getTargetClass(self):
        from gcloud.bigtable.row import ColumnRangeFilter
        return ColumnRangeFilter

    def _makeOne(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def test_constructor_defaults(self):
        column_family_id = object()
        row_filter = self._makeOne(column_family_id)
        self.assertTrue(row_filter.column_family_id is column_family_id)
        self.assertEqual(row_filter.start_column, None)
        self.assertEqual(row_filter.end_column, None)
        self.assertTrue(row_filter.inclusive_start)
        self.assertTrue(row_filter.inclusive_end)

    def test_constructor_explicit(self):
        column_family_id = object()
        start_column = object()
        end_column = object()
        inclusive_start = object()
        inclusive_end = object()
        row_filter = self._makeOne(column_family_id, start_column=start_column,
                                   end_column=end_column,
                                   inclusive_start=inclusive_start,
                                   inclusive_end=inclusive_end)
        self.assertTrue(row_filter.column_family_id is column_family_id)
        self.assertTrue(row_filter.start_column is start_column)
        self.assertTrue(row_filter.end_column is end_column)
        self.assertTrue(row_filter.inclusive_start is inclusive_start)
        self.assertTrue(row_filter.inclusive_end is inclusive_end)

    def test_constructor_bad_start(self):
        column_family_id = object()
        self.assertRaises(ValueError, self._makeOne,
                          column_family_id, inclusive_start=True)

    def test_constructor_bad_end(self):
        column_family_id = object()
        self.assertRaises(ValueError, self._makeOne,
                          column_family_id, inclusive_end=True)

    def test___eq__(self):
        column_family_id = object()
        start_column = object()
        end_column = object()
        inclusive_start = object()
        inclusive_end = object()
        row_filter1 = self._makeOne(column_family_id,
                                    start_column=start_column,
                                    end_column=end_column,
                                    inclusive_start=inclusive_start,
                                    inclusive_end=inclusive_end)
        row_filter2 = self._makeOne(column_family_id,
                                    start_column=start_column,
                                    end_column=end_column,
                                    inclusive_start=inclusive_start,
                                    inclusive_end=inclusive_end)
        self.assertEqual(row_filter1, row_filter2)

    def test___eq__type_differ(self):
        column_family_id = object()
        row_filter1 = self._makeOne(column_family_id)
        row_filter2 = object()
        self.assertNotEqual(row_filter1, row_filter2)

    def test_to_pb(self):
        from gcloud.bigtable._generated import bigtable_data_pb2 as data_pb2

        column_family_id = u'column-family-id'
        row_filter = self._makeOne(column_family_id)
        col_range_pb = data_pb2.ColumnRange(family_name=column_family_id)
        expected_pb = data_pb2.RowFilter(column_range_filter=col_range_pb)
        self.assertEqual(row_filter.to_pb(), expected_pb)

    def test_to_pb_inclusive_start(self):
        from gcloud.bigtable._generated import bigtable_data_pb2 as data_pb2

        column_family_id = u'column-family-id'
        column = b'column'
        row_filter = self._makeOne(column_family_id, start_column=column)
        col_range_pb = data_pb2.ColumnRange(
            family_name=column_family_id,
            start_qualifier_inclusive=column,
        )
        expected_pb = data_pb2.RowFilter(column_range_filter=col_range_pb)
        self.assertEqual(row_filter.to_pb(), expected_pb)

    def test_to_pb_exclusive_start(self):
        from gcloud.bigtable._generated import bigtable_data_pb2 as data_pb2

        column_family_id = u'column-family-id'
        column = b'column'
        row_filter = self._makeOne(column_family_id, start_column=column,
                                   inclusive_start=False)
        col_range_pb = data_pb2.ColumnRange(
            family_name=column_family_id,
            start_qualifier_exclusive=column,
        )
        expected_pb = data_pb2.RowFilter(column_range_filter=col_range_pb)
        self.assertEqual(row_filter.to_pb(), expected_pb)

    def test_to_pb_inclusive_end(self):
        from gcloud.bigtable._generated import bigtable_data_pb2 as data_pb2

        column_family_id = u'column-family-id'
        column = b'column'
        row_filter = self._makeOne(column_family_id, end_column=column)
        col_range_pb = data_pb2.ColumnRange(
            family_name=column_family_id,
            end_qualifier_inclusive=column,
        )
        expected_pb = data_pb2.RowFilter(column_range_filter=col_range_pb)
        self.assertEqual(row_filter.to_pb(), expected_pb)

    def test_to_pb_exclusive_end(self):
        from gcloud.bigtable._generated import bigtable_data_pb2 as data_pb2

        column_family_id = u'column-family-id'
        column = b'column'
        row_filter = self._makeOne(column_family_id, end_column=column,
                                   inclusive_end=False)
        col_range_pb = data_pb2.ColumnRange(
            family_name=column_family_id,
            end_qualifier_exclusive=column,
        )
        expected_pb = data_pb2.RowFilter(column_range_filter=col_range_pb)
        self.assertEqual(row_filter.to_pb(), expected_pb)


class TestTimestampRange(unittest2.TestCase):

    def _getTargetClass(self):
        from gcloud.bigtable.row import TimestampRange
        return TimestampRange

    def _makeOne(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def test_constructor(self):
        start = object()
        end = object()
        time_range = self._makeOne(start=start, end=end)
        self.assertTrue(time_range.start is start)
        self.assertTrue(time_range.end is end)

    def test___eq__(self):
        start = object()
        end = object()
        time_range1 = self._makeOne(start=start, end=end)
        time_range2 = self._makeOne(start=start, end=end)
        self.assertEqual(time_range1, time_range2)

    def test___eq__type_differ(self):
        start = object()
        end = object()
        time_range1 = self._makeOne(start=start, end=end)
        time_range2 = object()
        self.assertNotEqual(time_range1, time_range2)

    def test___ne__same_value(self):
        start = object()
        end = object()
        time_range1 = self._makeOne(start=start, end=end)
        time_range2 = self._makeOne(start=start, end=end)
        comparison_val = (time_range1 != time_range2)
        self.assertFalse(comparison_val)

    def _to_pb_helper(self, start_micros=None, end_micros=None):
        import datetime
        from gcloud._helpers import _EPOCH
        from gcloud.bigtable._generated import bigtable_data_pb2 as data_pb2

        pb_kwargs = {}

        start = None
        if start_micros is not None:
            start = _EPOCH + datetime.timedelta(microseconds=start_micros)
            pb_kwargs['start_timestamp_micros'] = start_micros
        end = None
        if end_micros is not None:
            end = _EPOCH + datetime.timedelta(microseconds=end_micros)
            pb_kwargs['end_timestamp_micros'] = end_micros
        time_range = self._makeOne(start=start, end=end)

        expected_pb = data_pb2.TimestampRange(**pb_kwargs)
        self.assertEqual(time_range.to_pb(), expected_pb)

    def test_to_pb(self):
        # Makes sure already milliseconds granularity
        start_micros = 30871000
        end_micros = 12939371000
        self._to_pb_helper(start_micros=start_micros,
                           end_micros=end_micros)

    def test_to_pb_start_only(self):
        # Makes sure already milliseconds granularity
        start_micros = 30871000
        self._to_pb_helper(start_micros=start_micros)

    def test_to_pb_end_only(self):
        # Makes sure already milliseconds granularity
        end_micros = 12939371000
        self._to_pb_helper(end_micros=end_micros)


class TestTimestampRangeFilter(unittest2.TestCase):

    def _getTargetClass(self):
        from gcloud.bigtable.row import TimestampRangeFilter
        return TimestampRangeFilter

    def _makeOne(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def test_constructor(self):
        range_ = object()
        row_filter = self._makeOne(range_)
        self.assertTrue(row_filter.range_ is range_)

    def test___eq__type_differ(self):
        range_ = object()
        row_filter1 = self._makeOne(range_)
        row_filter2 = object()
        self.assertNotEqual(row_filter1, row_filter2)

    def test___eq__same_value(self):
        range_ = object()
        row_filter1 = self._makeOne(range_)
        row_filter2 = self._makeOne(range_)
        self.assertEqual(row_filter1, row_filter2)

    def test_to_pb(self):
        from gcloud.bigtable._generated import bigtable_data_pb2 as data_pb2
        from gcloud.bigtable.row import TimestampRange

        range_ = TimestampRange()
        row_filter = self._makeOne(range_)
        pb_val = row_filter.to_pb()
        expected_pb = data_pb2.RowFilter(
            timestamp_range_filter=data_pb2.TimestampRange())
        self.assertEqual(pb_val, expected_pb)


class TestValueRegexFilter(unittest2.TestCase):

    def _getTargetClass(self):
        from gcloud.bigtable.row import ValueRegexFilter
        return ValueRegexFilter

    def _makeOne(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def test_to_pb(self):
        from gcloud.bigtable._generated import bigtable_data_pb2 as data_pb2

        regex = b'value-regex'
        row_filter = self._makeOne(regex)
        pb_val = row_filter.to_pb()
        expected_pb = data_pb2.RowFilter(value_regex_filter=regex)
        self.assertEqual(pb_val, expected_pb)


class TestValueRangeFilter(unittest2.TestCase):

    def _getTargetClass(self):
        from gcloud.bigtable.row import ValueRangeFilter
        return ValueRangeFilter

    def _makeOne(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def test_constructor_defaults(self):
        row_filter = self._makeOne()
        self.assertEqual(row_filter.start_value, None)
        self.assertEqual(row_filter.end_value, None)
        self.assertTrue(row_filter.inclusive_start)
        self.assertTrue(row_filter.inclusive_end)

    def test_constructor_explicit(self):
        start_value = object()
        end_value = object()
        inclusive_start = object()
        inclusive_end = object()
        row_filter = self._makeOne(start_value=start_value,
                                   end_value=end_value,
                                   inclusive_start=inclusive_start,
                                   inclusive_end=inclusive_end)
        self.assertTrue(row_filter.start_value is start_value)
        self.assertTrue(row_filter.end_value is end_value)
        self.assertTrue(row_filter.inclusive_start is inclusive_start)
        self.assertTrue(row_filter.inclusive_end is inclusive_end)

    def test_constructor_bad_start(self):
        self.assertRaises(ValueError, self._makeOne, inclusive_start=True)

    def test_constructor_bad_end(self):
        self.assertRaises(ValueError, self._makeOne, inclusive_end=True)

    def test___eq__(self):
        start_value = object()
        end_value = object()
        inclusive_start = object()
        inclusive_end = object()
        row_filter1 = self._makeOne(start_value=start_value,
                                    end_value=end_value,
                                    inclusive_start=inclusive_start,
                                    inclusive_end=inclusive_end)
        row_filter2 = self._makeOne(start_value=start_value,
                                    end_value=end_value,
                                    inclusive_start=inclusive_start,
                                    inclusive_end=inclusive_end)
        self.assertEqual(row_filter1, row_filter2)

    def test___eq__type_differ(self):
        row_filter1 = self._makeOne()
        row_filter2 = object()
        self.assertNotEqual(row_filter1, row_filter2)

    def test_to_pb(self):
        from gcloud.bigtable._generated import bigtable_data_pb2 as data_pb2

        row_filter = self._makeOne()
        expected_pb = data_pb2.RowFilter(
            value_range_filter=data_pb2.ValueRange())
        self.assertEqual(row_filter.to_pb(), expected_pb)

    def test_to_pb_inclusive_start(self):
        from gcloud.bigtable._generated import bigtable_data_pb2 as data_pb2

        value = b'some-value'
        row_filter = self._makeOne(start_value=value)
        val_range_pb = data_pb2.ValueRange(start_value_inclusive=value)
        expected_pb = data_pb2.RowFilter(value_range_filter=val_range_pb)
        self.assertEqual(row_filter.to_pb(), expected_pb)

    def test_to_pb_exclusive_start(self):
        from gcloud.bigtable._generated import bigtable_data_pb2 as data_pb2

        value = b'some-value'
        row_filter = self._makeOne(start_value=value, inclusive_start=False)
        val_range_pb = data_pb2.ValueRange(start_value_exclusive=value)
        expected_pb = data_pb2.RowFilter(value_range_filter=val_range_pb)
        self.assertEqual(row_filter.to_pb(), expected_pb)

    def test_to_pb_inclusive_end(self):
        from gcloud.bigtable._generated import bigtable_data_pb2 as data_pb2

        value = b'some-value'
        row_filter = self._makeOne(end_value=value)
        val_range_pb = data_pb2.ValueRange(end_value_inclusive=value)
        expected_pb = data_pb2.RowFilter(value_range_filter=val_range_pb)
        self.assertEqual(row_filter.to_pb(), expected_pb)

    def test_to_pb_exclusive_end(self):
        from gcloud.bigtable._generated import bigtable_data_pb2 as data_pb2

        value = b'some-value'
        row_filter = self._makeOne(end_value=value, inclusive_end=False)
        val_range_pb = data_pb2.ValueRange(end_value_exclusive=value)
        expected_pb = data_pb2.RowFilter(value_range_filter=val_range_pb)
        self.assertEqual(row_filter.to_pb(), expected_pb)


class Test_CellCountFilter(unittest2.TestCase):

    def _getTargetClass(self):
        from gcloud.bigtable.row import _CellCountFilter
        return _CellCountFilter

    def _makeOne(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def test_constructor(self):
        num_cells = object()
        row_filter = self._makeOne(num_cells)
        self.assertTrue(row_filter.num_cells is num_cells)

    def test___eq__type_differ(self):
        num_cells = object()
        row_filter1 = self._makeOne(num_cells)
        row_filter2 = object()
        self.assertNotEqual(row_filter1, row_filter2)

    def test___eq__same_value(self):
        num_cells = object()
        row_filter1 = self._makeOne(num_cells)
        row_filter2 = self._makeOne(num_cells)
        self.assertEqual(row_filter1, row_filter2)

    def test___ne__same_value(self):
        num_cells = object()
        row_filter1 = self._makeOne(num_cells)
        row_filter2 = self._makeOne(num_cells)
        comparison_val = (row_filter1 != row_filter2)
        self.assertFalse(comparison_val)


class TestCellsRowOffsetFilter(unittest2.TestCase):

    def _getTargetClass(self):
        from gcloud.bigtable.row import CellsRowOffsetFilter
        return CellsRowOffsetFilter

    def _makeOne(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def test_to_pb(self):
        from gcloud.bigtable._generated import bigtable_data_pb2 as data_pb2

        num_cells = 76
        row_filter = self._makeOne(num_cells)
        pb_val = row_filter.to_pb()
        expected_pb = data_pb2.RowFilter(cells_per_row_offset_filter=num_cells)
        self.assertEqual(pb_val, expected_pb)


class TestCellsRowLimitFilter(unittest2.TestCase):

    def _getTargetClass(self):
        from gcloud.bigtable.row import CellsRowLimitFilter
        return CellsRowLimitFilter

    def _makeOne(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def test_to_pb(self):
        from gcloud.bigtable._generated import bigtable_data_pb2 as data_pb2

        num_cells = 189
        row_filter = self._makeOne(num_cells)
        pb_val = row_filter.to_pb()
        expected_pb = data_pb2.RowFilter(cells_per_row_limit_filter=num_cells)
        self.assertEqual(pb_val, expected_pb)


class TestCellsColumnLimitFilter(unittest2.TestCase):

    def _getTargetClass(self):
        from gcloud.bigtable.row import CellsColumnLimitFilter
        return CellsColumnLimitFilter

    def _makeOne(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def test_to_pb(self):
        from gcloud.bigtable._generated import bigtable_data_pb2 as data_pb2

        num_cells = 10
        row_filter = self._makeOne(num_cells)
        pb_val = row_filter.to_pb()
        expected_pb = data_pb2.RowFilter(
            cells_per_column_limit_filter=num_cells)
        self.assertEqual(pb_val, expected_pb)


class TestStripValueTransformerFilter(unittest2.TestCase):

    def _getTargetClass(self):
        from gcloud.bigtable.row import StripValueTransformerFilter
        return StripValueTransformerFilter

    def _makeOne(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def test_to_pb(self):
        from gcloud.bigtable._generated import bigtable_data_pb2 as data_pb2

        flag = True
        row_filter = self._makeOne(flag)
        pb_val = row_filter.to_pb()
        expected_pb = data_pb2.RowFilter(strip_value_transformer=flag)
        self.assertEqual(pb_val, expected_pb)


class TestApplyLabelFilter(unittest2.TestCase):

    def _getTargetClass(self):
        from gcloud.bigtable.row import ApplyLabelFilter
        return ApplyLabelFilter

    def _makeOne(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def test_constructor(self):
        label = object()
        row_filter = self._makeOne(label)
        self.assertTrue(row_filter.label is label)

    def test___eq__type_differ(self):
        label = object()
        row_filter1 = self._makeOne(label)
        row_filter2 = object()
        self.assertNotEqual(row_filter1, row_filter2)

    def test___eq__same_value(self):
        label = object()
        row_filter1 = self._makeOne(label)
        row_filter2 = self._makeOne(label)
        self.assertEqual(row_filter1, row_filter2)

    def test_to_pb(self):
        from gcloud.bigtable._generated import bigtable_data_pb2 as data_pb2

        label = u'label'
        row_filter = self._makeOne(label)
        pb_val = row_filter.to_pb()
        expected_pb = data_pb2.RowFilter(apply_label_transformer=label)
        self.assertEqual(pb_val, expected_pb)