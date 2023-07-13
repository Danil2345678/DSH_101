users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

users_visits = {
    "Общее количество": len(users),
    "Уникальные посещения": len(set(users))
}
print(users_visits)
