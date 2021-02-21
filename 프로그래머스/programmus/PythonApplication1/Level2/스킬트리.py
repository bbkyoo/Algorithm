#def solution(skill, skill_trees): 
#    skill_lt = list(skill)
#    count =  len(skill_trees)
#    for i in range(len(skill_trees)):
#        for j in range(len(skill_trees[i])):
#            if skill_trees[i][j] not in skill_lt:
#                skill_trees[i] = skill_trees[i].replace(skill_trees[i][j], 'a')

#    for i in range(len(skill_trees)):
#        temp = ''
        
#        for j in range(len(skill_trees[i])):
#            if skill_trees[i][j] != 'a':
#                temp += skill_trees[i][j]

#        temp = list(temp)    
#        for k in range(len(temp)):
#            if temp[k] != skill_lt[k]:
#                count -= 1
#                break
        
#    return count


def solution(skill, skill_trees):

  answer = 0

  for i in skill_trees:
    list = []
    fin = True
    
    for j in range(len(i)):
      if i[j] in skill:
      	list.append(i[j])

    for k in range(len(list)):
      if list[k] != skill[k]:
        fin = False
        break

  if fin == True:
  	answer += 1

  return answer




