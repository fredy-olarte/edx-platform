from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('lms.djangoapps', 'learner_dashboard.programs')

from lms.djangoapps.learner_dashboard.programs import *
