# Workspace access control

All resources on Beamlit are logically regrouped in a **workspace,** which is the highest possible level of tenancy. Your organization will usually operate within one single workspace, but it is not necessarily the case when dealing with multiple business units or end-clients for example.

Users are added to a workspace with certain permissions on the workspace resources inherited from their role.

## User roles

There are two roles that a user can have in a workspace: **admin** and **member**.

Admins have **complete access** in the workspace, on all workspace resources. They can also modify all workspace settings, including inviting other team members. More specifically, admins have all the permissions that members have, in addition to:

- inviting and removing users
- changing user’s permissions
- adding and removing integrations
- changing the workspace name
- deleting the workspace

Members can view the workspace settings but not edit them. They are also able to **view and modify** the following resources inside a workspace:

- models (including querying them)
- model deployments
- policies
- environments
- clusters

## Invite a member

Admins can invite team members via their email address. They will be prompted for the role to give the user. 

![Screenshot 2024-10-15 at 5.22.37 PM.png](Workspace%20access%20control/Screenshot_2024-10-15_at_5.22.37_PM.png)

The invitee will receive an email to allow them to accept the invitation on Beamlit console. They will not be able to access workspace resources until they have manually accepted the invitation. If the user doesn’t have a Beamlit account already, they will be asked to signup first.

## Delete a workspace

Admins can delete a workspace on Beamlit console from the workspace settings. **This action cannot be undone once it is done**.