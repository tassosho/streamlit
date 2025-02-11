# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022-2024)
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

import requests

import streamlit as st

url = "https://www.w3schools.com/html/mov_bbb.mp4"
file = requests.get(url).content
st.video(file)

# Test start time with widget
timestamp = st.number_input("Start Time (in seconds)", min_value=0, value=6)
st.video(url, start_time=int(timestamp))
