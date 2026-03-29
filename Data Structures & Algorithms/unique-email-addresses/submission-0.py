class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        email_map = {}

        for email in emails:
            names = email.split("@")
            cleaned_local_name = names[0].replace(".", "")
            cleaned_local_name = cleaned_local_name.split("+")[0]

            cleaned_name = cleaned_local_name + "@" + names[1]
            email_map[cleaned_name] = 1

        return len(email_map)