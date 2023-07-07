# from time import time
# import asyncio
# import aiohttp

# target_domain = "changwon.ac.kr"
# wordlist = "./서브도메인_리스트.txt"

# async def asnyc_func(domains):
#     connect=aiohttp.TCPConnector(limit_per_host=10)
#     async with aiohttp.ClientSession(connector=connect) as s:
#         futures=[
#             asyncio.create_task(discover_url(s,f"https://{domain}.{target_domain}"))
#             for domain in domains:
#         ]
#         results=await asyncio.gather(*futures)

# async def discover_urls(s,domain):
#     try:
#         async with s.get(domain) as r:
#             if r.status==200:
#                 output=(domain, r.status)
#                 print(output)
#                 return output
#             else:
#                 raise Exception("status_code", r.status)
# except aiohttp client_exceptions.ClientConnetionError as e:
