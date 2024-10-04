# 2491. Divide Players Into Teams of Equal Skill

class Solution:
    def dividePlayers(self, skill):
        # Sort the skill array
        skill.sort()
        
        # Get the target sum which is the sum of the first and last element
        target_sum = skill[0] + skill[-1]
        total_chemistry = 0
        
        # Iterate through the array and pair players from both ends
        for i in range(len(skill) // 2):
            if skill[i] + skill[-i-1] != target_sum:
                return -1
            # Add the product of the two paired skills to total_chemistry
            total_chemistry += skill[i] * skill[-i-1]
        
        return total_chemistry
