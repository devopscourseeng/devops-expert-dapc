# How to send the invitations (GitHub and Jira)

A guide for the instructor. Every participant needs **two invitations**, one for the GitHub repository and one for the Jira project. Send them several days before Session 5, so there is time to fix problems.

| What | Where |
|---|---|
| GitHub repository | https://github.com/devopscourseeng/devops-expert-dapc |
| Jira project (key SCRUM) | https://devopscourseeng.atlassian.net/jira/software/projects/SCRUM/boards/1 |
| Guide for participants | [setup-tools.md](setup-tools.md) |

## Before you start

- [ ] You are an **admin** of the GitHub repository and an **admin** of the Jira site.
- [ ] You have a list of participants: full name, **email**, and **GitHub username** (ask for it, one line per person).
- [ ] Every participant who has no GitHub account knows they must create a free one first: https://github.com/signup
- [ ] Do not write participants' emails or names in the repository. It is public.

## Step 1. Collect the details

Send this short message to each participant, or to the group:

> Hello! To prepare Session 5, please send me:
> 1. The email you want to use for Jira
> 2. Your GitHub username (create a free account at https://github.com/signup if you do not have one)
>
> You will get two invitations, one from GitHub and one from Jira. Please accept both before the session.

## Step 2. Invite to GitHub (Write access)

1. Open the repository and go to **Settings → Collaborators** (under "Access").
2. Click **Add people**.
3. Type the participant's **GitHub username**. You can also type an email, but a username is more reliable.
4. Choose the role **Write**, then click **Add**.
5. Repeat for each participant.

GitHub sends an email invitation. The invitation expires after 7 days. If it expires, send it again.

**Check:** in **Settings → Collaborators**, people who have not accepted appear as **Pending invite**.

## Step 3. Invite to Jira (SCRUM project)

1. Open the SCRUM project and go to **Project settings → People** (in older layouts: **Project settings → Access**).
2. Click **Add people**.
3. Type each participant's **email**. Use the same email they will sign in with.
4. Choose the role **Member** and click **Add**.
5. If Jira asks for product access, give **Jira** (Jira Software) access.
6. If a participant does not appear as a user yet, you can also invite from **admin.atlassian.com → Users → Invite users**, then add them to the project.

Atlassian sends an email invitation to the exact email you entered. The participant must create or sign in to an Atlassian account **with that same email**.

**Check:** in **Project settings → People**, each participant is listed with the Member role. Users who have not accepted show as **Invited**.

## Step 4. Send the welcome email

Fill in the date and time, and send it to everyone:

> Subject: DAPC Session 5: please accept your two invitations
>
> Hello,
>
> Our next session is on **[date and time]**. Before the session, please do this:
> 1. Accept the **GitHub** invitation (email from GitHub).
> 2. Accept the **Jira** invitation (email from Atlassian). Use the same email I invited.
> 3. If you can, read the setup guide: https://github.com/devopscourseeng/devops-expert-dapc/blob/main/docs/setup-tools.md
>
> If an invitation does not arrive, check your spam folder and tell me.
>
> See you soon!

## Step 5. Track who accepted

Keep this table in a private place (not in the repository):

| Participant | GitHub invited | GitHub accepted | Jira invited | Jira accepted |
|---|---|---|---|---|
| | | | | |

- Check **Settings → Collaborators** and **Project settings → People** the day after sending, and again **two days before** the session.
- Send a short reminder to anyone who has not accepted both invitations.

## Common problems

| Problem | What to do |
|---|---|
| The GitHub invitation does not arrive | Check the spam folder. Send the invitation again to the **username** instead of the email. Participants can also open https://github.com/devopscourseeng/devops-expert-dapc and accept from the banner at the top. |
| The GitHub invitation expired | Cancel the pending invite in **Settings → Collaborators** and add the person again. |
| The participant used a different email in Jira | Remove the user and invite the correct email, or ask the participant to add the invited email to their Atlassian account. |
| A participant cannot create an account | Ask them to try a different browser or email, and tell you the exact error. |
| The role is wrong | In GitHub, change the role to **Write** in **Settings → Collaborators**. In Jira, change the role to **Member** in **Project settings → People**. |

## When everyone has accepted

- [ ] All 6 participants appear as collaborators with **Write** access in GitHub.
- [ ] All 6 participants are Members of the SCRUM project in Jira.
- [ ] The starter tickets are created and assigned (see the plan, Session 5 action items).
