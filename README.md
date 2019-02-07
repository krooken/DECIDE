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
