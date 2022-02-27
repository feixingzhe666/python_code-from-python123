deposit = int(input())  # 存款金额本金
years = int(input())    # 存款年数
interest_rates = float(input())  # 年利率
new_deposit = deposit            # 初始本金
for i in range(years):           # 逐年计算新的一年的本息合计
    new_deposit = new_deposit*(1 + interest_rates)  # 每年的本息合计总收益
interest = new_deposit - deposit  # 总收益中去掉初始本金结果为利息
print("利息={:.2f}".format(interest))

# 用幂运算实现
deposit = int(input())  # 存款金额本金
years = int(input())
interest_rates = float(input())
total = deposit * pow((1 + interest_rates), years)
interest = total - deposit
print("利息={:.2f}".format(interest))
