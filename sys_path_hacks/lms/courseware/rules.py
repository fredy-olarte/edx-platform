from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('lms.djangoapps', 'courseware.rules')

from lms.djangoapps.courseware.rules import *
