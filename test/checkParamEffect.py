import json
import glob
import os
import unittest

def checkEffect(jPolicy):
    # This function validates that a policy or initiative has set the effect as parameterized.
    pyPolicy = json.loads(jPolicy)
    policyEffect = pyPolicy['properties']['policyRule']['then']['effect']
    # Ensure the policy effect is parameterized
    check = "parameters" in policyEffect
    return check


def getAllPolicies(path):
    # The function pulls the list of all policies which exist in the path folder.
    searchStr = path + "/**/*.json"
    typeStr = "Microsoft.Authorization/policyDefinitions"
    policyList = []
    fileList = glob.glob(searchStr)
    # Check each json file in directory
    for item in fileList:
        f = open(item)
        raw = f.read()
        obj = json.loads(raw)
        # If the file has the 'type' attribute and it is equal to typeStr, add to list
        try:
            resType = obj['type']
            typeCheck = resType == typeStr
        except:
            typeCheck = False
        if typeCheck:
            policyList.append(item)
        else:
            continue
    return policyList

# Main Test
print("Getting all policy files...")
path = "samples"
policies = getAllPolicies(path)
response = True
for path in policies:
    fileName = os.path.basename(path)
    print("Checking: " + fileName)
    f = open(path)
    policy = f.read()
    if checkEffect(policy):
        continue
    else: 
        response = False
        print("    Please parameterize this policy's effect.")

if response:
    print("All policy effects are appropriately parameterized.")
else:
    raise Exception("One or more of your policy definitions does not have its effect parameterized.")
