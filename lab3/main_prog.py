import vk_get_userfriends
import vk_get_userid
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


user_domain = input("Введите имя пользователя \n ")
client_object1 = vk_get_userid.VkUserId(user_domain)
client_object1.execute()

print(client_object1.response_content)
print("user_id = ", client_object1.user_id)


client_object2 = vk_get_userfriends.VkUserFriends(client_object1.user_id)
client_object2.execute()

unique_ages_list = sorted(set(client_object2.ages_list))
for el in unique_ages_list:
    print(el, ":", "#"*client_object2.ages_list.count(el))

fig, ax = plt.subplots()
plt.hist(client_object2.ages_list, max(client_object2.ages_list),color="gray", rwidth=1)
ax.set_xlabel('Age')
ax.set_ylabel('count')
ax.set_title("Histogram of Ages")
fig.tight_layout()
plt.show()


print('Script Ends Here')
