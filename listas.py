#criando listas em python
#"apprend' adiciona o numero no final da lista
#"sum" = soma
#
nums = []
for i in range(5):
    num = int(input(f"Digite o {i+1} numero:"))
    nums.append(num)
for num in  nums:
    print(num)
    
soma = sum(nums)
print(soma)

media = sum(nums)/len(nums)
print(media)