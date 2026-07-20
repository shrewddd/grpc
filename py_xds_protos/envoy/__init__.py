# Copyright 2026 gRPC authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

try:
    from tests import bazel_namespace_package_hack
except ImportError:
    from src.python.grpcio_tests.tests import bazel_namespace_package_hack
bazel_namespace_package_hack.sys_path_to_site_dir_hack()
