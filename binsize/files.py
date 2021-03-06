from rest_framework_csv.renderers import CSVStreamingRenderer

class FileRenderCN(CSVStreamingRenderer):
    header = [
        'bin_size',
        'bin_size_w',
        'bin_size_d',
        'bin_size_h',
        'creater',
        'create_time',
        'update_time'
    ]
    labels = dict([
        ('bin_size', u'库位尺寸名称'),
        ('bin_size_w', u'库位尺寸长度'),
        ('bin_size_d', u'库位尺寸宽度'),
        ('bin_size_h', u'库位尺寸高度'),
        ('creater', u'创建人'),
        ('create_time', u'创建时间'),
        ('update_time', u'更新时间'),
    ])

class FileRenderEN(CSVStreamingRenderer):
    header = [
        'bin_size',
        'bin_size_w',
        'bin_size_d',
        'bin_size_h',
        'creater',
        'create_time',
        'update_time'
    ]
    labels = dict([
        ('bin_size', u'Bin Size'),
        ('bin_size_w', u'Bin Wide'),
        ('bin_size_d', u'Bin Depth'),
        ('bin_size_h', u'Bin Height'),
        ('creater', u'Creater'),
        ('create_time', u'Create Time'),
        ('update_time', u'Update Time'),
    ])
