import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('Interactive Widgets')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!!!'

text = st.text_input('あなたの趣味を教えて下さい.')
condition = st.slider('あなたの今の調子は？', 0, 100, 50)

'あなたの趣味：', text
'コンディション：', condition

st.write('Display Image')

if st.checkbox('Show Image'):
    img = Image.open('sample.jpg')
    st.image(img, caption='Kohei Imanishi', use_column_width=True)
    

# df = pd.DataFrame({
#     '1列目': [1, 2, 3, 4],
#     '2列目': [10, 20, 30, 40]
# })

# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )

# st.map(df)

# st.line_chart(df)

# st.table(df.style.highlight_max(axis=0))
# st.dataframe(df.style.highlight_max(axis=0))

# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """