# Introduction to Payload, a Headless CMS and App Framework
![Featued image for: Introduction to Payload, a Headless CMS and App Framework](https://cdn.thenewstack.io/media/2024/09/cda64814-getty-images-0udnq131w5g-unsplash-1024x724.jpg)
One of the interesting things about web development has always been the attempt to merge the worlds of visual design with that of data design. While they need to come together in websites and web apps, they are quite separate disciplines. Frameworks like [Ruby on Rails](https://thenewstack.io/return-to-the-rails-way-installing-ruby-on-rails-in-2024/) consistently jump back and forth over the fence in an effort to pull them together.

[Payload CMS](https://payloadcms.com/) bravely describes itself as a “headless CMS and application framework.” Although we don’t refer to user interfaces as “heads,” [headless](https://thenewstack.io/headless-cms-vs-no-code-website-builders/) just refers to a framework with no exclusive frontend. A content management system (CMS) is just a framework that manipulates structured data. If the data is a blog, then the content being managed are posts, for example.
The [What is Payload](https://payloadcms.com/docs/getting-started/what-is-payload) page does a good job of presenting this dilemma, as well as trying to explain its own angle. It hits pay dirt when it recognises that a CMS tends to “bind the presentation of your content to the storage of your content.” Accordingly, what Payload aims to do is to work with whatever frontend you want to use.

As of now, Payload is between some breaking changes and version 3, so old documentation may be out of date. Following the instructions as I did, I got an older version. This will no doubt be smoothed out. Just check its [Discord channel](https://discord.com/invite/r6sCXqVk3v) for the latest information.

## Installation
As yet, the [installation](https://payloadcms.com/docs/getting-started/installation) pre-requisite options are a bit narrow for databases, but there is one relational and one document-based example to choose from:

On my trusty MacBook, I installed a community [MongoDB](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/) via Homebrew:

Then I started Mongo up by adding it as a service:

We can see the connection string as the URL, so we should be able to set up Payload.

In another browser tab, I installed the Payload app:

I set up a demo project and soon we are ready to launch:

One of the example projects failed because it expected Discord! As I’ve said, because of the upcoming changes some of the documentation and videos don’t quite match up yet. That’s a good thing of course — the project is very active. I selected the payload-demo template, which was fine.

Then “yarn dev” runs the project:

After MongoDB is connected to, it starts up both the payload admin (at localhost:3000/admin) as well as the demonstration app (marked as Next.js app, the React framework used for the template).

## The Payload App
Going straight into the app we see:

At this point, there is no content, so you are guided to the admin dashboard to start making some. The admin dashboard allows me to create an Admin role or User role, with email.

The dashboard itself helps to explain what Payload is actually about:

Payload organizes everything into sets of types in collections. This include Pages and Users. We can create new types and start using them immediately, as we will do.

There is a slight confusion here: To start things off, you press the link to “Seed the database,” and you will get lots of demo content. That will clean out anything that already exists. You also need to make a “home” page, otherwise you will just see the default template page from above, which will perhaps make you think you have no content, when you have.

Once I understood the system, I created some simple if uninspired content on a Page type:

Once you use the admin interface to add to the collections, you can then Publish any changes (commit them). This will automatically update your site.

## Doing Everything in Code
Now at this stage, I’ve not done much more than you could do with, say, [Publii](https://thenewstack.io/jamstack-style-build-a-website-with-netlify-and-publii/), which also acts like a classic CMS. However, there are two things that stand out in Payload. Not only can you talk to it in REST, you can reuse parts of Payload that blur the distinction between who owns what. And you can do everything in code, which is where we go now.

For example, you can see that Users is a collection type, available for use by us:

And where are these registered? All in the `payload.config.ts`
file. First they are imported, then (as you can see below) added into the known collections:

Within the Users folder, we have a basic index.ts file, which defines the Users type. While this includes quite a lot of Typescript, most of it is just describing the admin access. Payload allows quite a lot of granular access control:

1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859 |
import type { CollectionConfig } from 'payload/types' import { admins } from '../../access/admins' import { anyone } from '../../access/anyone' import adminsAndUser from './access/adminsAndUser' import { checkRole } from './checkRole' import { ensureFirstUserIsAdmin } from './hooks/ensureFirstUserIsAdmin' import { loginAfterCreate } from './hooks/loginAfterCreate' const Users: CollectionConfig = { slug: 'users', admin: { useAsTitle: 'name', defaultColumns: ['name', 'email'], }, access: { read: adminsAndUser, create: anyone, update: adminsAndUser, delete: admins, admin: ({ req: { user } }) => checkRole(['admin'], user), }, hooks: { afterChange: [loginAfterCreate], }, auth: true, fields: [ { name: 'name', type: 'text', }, { name: 'roles', type: 'select', hasMany: true, defaultValue: ['user'], options: [ { label: 'admin', value: 'admin', }, { label: 'user', value: 'user', }, ], hooks: { beforeChange: [ensureFirstUserIsAdmin], }, access: { read: admins, create: admins, update: admins, }, }, ], timestamps: true, } export default Users |
However, we are going to pare this down and create our own collection type, with no admin or hooks.
Let’s say we just want a type called Members. I’ll make the appropriate folder and create a hacked down index.ts:

123456789101112131415161718 |
import type { CollectionConfig } from 'payload/types' const Members: CollectionConfig = { slug: 'members', fields: [ { name: 'name', type: 'text', }, { name: 'membership', type: 'number', }, ], timestamps: true, } export default Members |
This just describes a type with a name and numeric membership field. Payload does a lot of work through the different fields.
The server detected the changes:

And immediately the collections recognised the new type within the admin panel:

And we can manipulate members like any other collection type:

One last thing. Let’s access our new member via REST:

So we are locked out. But wait a minute … remember the granular access we removed to make the Member collection simple? Let’s try to put a bit back in:

12345678910111213141516171819202122 |
import type { CollectionConfig } from 'payload/types'import { anyone } from '../../access/anyone'const Members: CollectionConfig = { slug: 'members', access: { read: anyone, }, fields: [ { name: 'name', type: 'text', }, { name: 'memebership', type: 'number', }, ], timestamps: true,}export default Members |
All I did was add the import for “anyone” and add that access. Now let’s try:
Pretty good. We created a new collection, saw it in the admin console, created an entry for it and even requested it via REST. So this content is now available for my site.

## Conclusion
As I said earlier, Payload is currently transitioning to version 3, so it may make sense to hold out for a bit before investigating it. That said, the idea is already quite a strong one if you don’t insist that your frontend and backend endure a shotgun wedding.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)