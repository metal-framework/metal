self_revision_prompt_template = """You are an expert Python developer who specializes in writing matplotlib code based on a given picture. 
I have a code for implementing the reference picture as follows:\n```python\n{code}\n```\n\n
I also show you the reference picture that I want to reproduce.
\n\nNow, please judge whether the python code is able to reproduce the reference picture. 
The difference may cover, but not be limited to, the following aspects:\n1. Layout\n2. Chart Type\n3. Data Trend or Pattern\n4. Additional Features: such as legends, colormaps, tick labels, or text annotations that contribute to the figure's clarity or aesthetic appeal.
\n\n- If the python code can reproduce the reference, please output it directly.
\n\n- If there are discrepancies, first list the specific differences.
Then, modify the existing code to address these differences, ensuring the revised code is capable of reproducing the reference picture. 
Finally, output the revised code.
"""


