# Create a sample collection
# users ={'Hans':'active','Rudransh':'inactive','shiva':'active'}

# # stratger to get only active
# # first one is to copy the iteration and then delete the the inactive one
# for user,status in users.copy().items():
#     if status=='inactive':
#         del users[user]


# # Strategy:Create a new collection
# active_users={}
# for user,status in users.items():
#     if status=='active':
#         active_users[user]=status
        

# print(active_users)


