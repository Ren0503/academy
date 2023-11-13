# Database Schema

<figure><img src="../.gitbook/assets/ClassDiagram.drawio.png" alt=""><figcaption></figcaption></figure>

## Virtual

* Page is profile with a role is PAGE.
* A person who is someone's friend who has a Relation with someone has type equal FRIEND. Similarly, with Follow, and Block.
* When someone likes a page, a relation created with the type is LIKE.
* When someone creates a page, a relation created with the type is OWNER.

## Relations

### One to Many & Many to One

* One Profile has many Friends, Following, Followers, and Blocked Users.
* One Profile has many Pages and could like many Pages.
* One Profile/Page has many Posts, Reacts, and Comments.
* One Post has many Reacts and Comments.
* One Comment has many Reacts.
* One Profile/Page can join many groups.
* One Profile with One Group only has One Member.
