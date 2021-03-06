# DECIDE(); Launch Interceptor Program (exercise in software engineering)

DECIDE() is a part of a hypothetical anti-ballistic missile system.
DECIDE() will generate a boolean signal which determines whether an interceptor should be
launched based upon input radar tracking information. This radar tracking information is available
at the instant the function is called.

DECIDE() determines which combination of the several possible Launch Interceptor Conditions (LIC’s) are relevant to the immediate situation. The interceptor launch button is normally
considered locked; only if all relevant combinations of launch conditions are met will the launchunlock signal be issued.

DECIDE() determines whether each of fifteen LIC’s is true for an input set of up to 100
planar data points representing radar echoes. The fifteen elements of a Conditions Met Vector
(CMV) will be assigned boolean values true or false; each element of the CMV corresponds to one
LIC’s condition.

The input Logical Connector Matrix (LCM), defines which individual LIC’s must be considered jointly in some way. The LCM is a 15x15 symmetric matrix with elements valued ANDD,
ORR, or NOTUSED. The combination of LCM and CMV is stored in the Preliminary Unlocking
Matrix (PUM), a 15x15 symmetric matrix.

Another input, the Preliminary Unlocking Vector (PUV) represents which LIC actually matters
in this particular launch determination. Each element of the UV indicates how to combine the PUM
values to form the corresponding element of the Final Unlocking Vector (FUV), a 15-element
vector. If, and only if, all the values in the FUV are true, should the launch-unlock signal be
generated.

## Testing

The python unittest framework is used to test the code. For every function or method found in the decide folder,
a corresponding test case file is found in the test folder. Each test case contains test methods that test different
aspects of the function/method under test. All tests can be run by running either of
```
run_tests.sh
```
and
```
run_tests.bat
```
Alternatively, run ``python -m unittest discover`` directly in a terminal from the root folder of the Git repository.

## Project guidelines

All commits shall have a short and concise summary, preferably less than 70 characters.
If additional explanation is needed, leave a blank line between the summary and the detailed explanations.
Try to explain why a change was made, if not really obvious.
(The 'what' and 'how' is less important since it usually is included in the commit diff.)

Prefix the commit summary with ``ADD:``, ``FIX:``, ``DOC:``, or ``REFACTOR:`` if it is a new feature, bug fix, documentation, or refactor, respectively.
Try to separate the commits into parts such that the prefix is consistent with the commit contents.
