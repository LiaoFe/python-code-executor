from pyston import PystonClient, File
import asyncio


async def main():
    client = PystonClient()
    
    code = \
"""
import pandas as pd
import numpy as np

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
# while True:
#     print("ok")
"""
    
    output = await client.execute("python", [File(code)])
    print(output)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
