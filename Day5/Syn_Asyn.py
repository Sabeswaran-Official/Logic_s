# supervised ,unsupervised & self-supervised  (LLM) 

# Synchronous  -  can process one task at a time 
'''import time
def syn():
    print("Hi")
    time.sleep(3)
    print("Come here")
def syn1():
    print("What do you want")
    time.sleep(3)
    print("Say anything")

syn()
syn1()'''

# Asynchronous
import asyncio
async def syn():
    print("Hi")
    await asyncio.sleep(3)
    print("Come here")
async def syn1():
    print("What do you want")
    await asyncio.sleep(5)
    print("Say anything")

async def main():
    await asyncio.gather(syn(),syn1())

asyncio.run(main())