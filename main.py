import pandas as pd
from tqdm import tqdm
import logging

# 设置日志级别为INFO
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



# 把这里改成你的钱包文件路径
myaddress_df = pd.read_csv('myaddress.csv')

initial_df = pd.read_csv('initialList.csv')
sybil_df = pd.DataFrame()
logging.info('开始查询账户数否存在于女巫名单中...')
for index, row in tqdm(myaddress_df.iterrows(), total=myaddress_df.shape[0]):
    my_address = row['ADDRESS']
    match_df = initial_df[initial_df['ADDRESS'].str.contains(my_address)]
    sybil_df = pd.concat([sybil_df, match_df], ignore_index=True)
if sybil_df.shape[0] == 0:
    logging.info('查询完成！没有匹配的账户！')
    exit()
logging.warning(f'查询完成！共有{sybil_df.shape[0]}个匹配的账户。')
logging.info(sybil_df.head())
sybil_df.to_csv('sybil.csv', index=False)
logging.info('女巫名单已经保存到sybil.csv 文件中！')