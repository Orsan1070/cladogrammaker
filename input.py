evocolor = "#3183b5"
variantcolor = "#b55931"
megacolor = "#ac31b5"
deathcolor = "#a82e2e"
changecolor = "#b0b531"
gendercolor = "#8a97ff"
formcolor = "#31b53b"
gmaxcolor = "#dd72bb"
humanevocolor = "#5e31b5"
createdcolor = "#979797"
unknowncolor = "#0b7014"
splitcolor = "#e4a213"
incarnatescolor = "#e6c78a"
imbuedcolor = "#ff4646"
wormholecolor = "#73E6E6"

import random

def randomsuffix(max):
    output = random.randint(0,max)
    if output == 0:
        output = ""
    else: 
        output = "_" + "{:02d}".format(output)
    return output

vivillon = randomsuffix(18)
florges = randomsuffix(4)
sawsbuck = randomsuffix(3)

dogs = (
    (
        (
            (
                {"color": evocolor, "tree": [{"id": "lillipup", "tree": "0506.png"}, "0507.png", "0508.png"]},
                "0676.png"
            ),
            (
                {"color": evocolor, "tree": [{"id": "maschiff", "tree": "0942.png"}, "0943.png"]},
                (
                    (
                        {"color": evocolor, "tree": ["0228.png", {"color": megacolor, "tree": ["0229.png","0229_01.png"]}]},
                        {"color": variantcolor, "tree": (
                            {"color": evocolor, "tree": [{"id": "growlithe", "tree": "0058.png"},"0059.png"]},
                            {"color": evocolor, "tree": [{"id": "hisuigrowlithe", "tree": "0058_01.png"},"0059_01.png"]}
                        )},
                    ),
                    (
                        {"color": evocolor, "tree": ["0309.png", {"color": megacolor, "tree": ["0310.png","0310_01.png"]}]},
                        {"color": evocolor, "tree": [{"id": "yamper", "tree": "0835.png"}, "0836.png"]},
                    )
                ),
            ),
        ),
        {"color": deathcolor, "tree": ["mysterybeast.png", {"color": changecolor, "tree": ("0243.png","0244.png","0245.png")}]},
    ),
    (
        (
            {"color": evocolor, "tree": ["0926.png", "0927.png"]},
            {"color": gendercolor, "tree": ({"color": formcolor, "tree": ["0888.png", "0888_01.png"]}, {"color": formcolor, "tree": ["0889.png", "0889_01.png"]})},
        ),
        (
            (
                {"color": evocolor, "tree": ["0209.png", "0210.png"]},
                (
                    {"color": evocolor, "tree": ["0684.png", "0685.png"]},
                    "0235.png"
                )
            ),
            (
                (
                    {"color": evocolor, "tree": ["0447.png", {"color": megacolor, "tree": ["0448.png","0448_01.png"]}]},
                    {"color": changecolor, "tree": ["mysteryokidogi.png","1014.png"]}
                ),
                {"color": evocolor, "tree": [{"id": "rockruff", "tree": "0744.png"}, {"anchor": True, "tree": ("0745.png", "0745_01.png", "0745_02.png")}]}
            )
        )
    )
)

foxes = (
    (
        {"color": variantcolor, "tree": (
            {"color": evocolor, "tree": ["0037.png","0038.png"]},
            {"color": evocolor, "tree": ["0037_01.png","0038_01.png"]}
        )},
        (
            {"color": evocolor, "tree": ["0063.png", "0064.png", {"color": megacolor, "tree": ["0065.png","0065_01.png"]}]},
            (
                {"color": evocolor, "tree": ["0570.png",{"anchor": True, "tree": ({"id": "zoroark", "tree": "0571.png"},{"color": deathcolor, "colorroot": True, "tree": {"color": evocolor, "tree": ["0570_01.png",{"id": "hisuizoroark", "tree": "0571_01.png"}]}})}]},
                {"color": evocolor, "tree": ["0653.png","0654.png",{"color": megacolor, "tree": ["0655.png","0655_01.png"]}]},
            ),
        ),
    ),
    {"color": evocolor, "tree": ["0827.png", "0828.png"]},
)

canids = (
    (
        (
            foxes
        ),
        dogs
    ),
    {"color": evocolor, "tree": ["0133.png", {"anchor": True, "tree": ({"color": gmaxcolor, "colorroot": True, "tree": "gmaxeevee.png"}, "0134.png", "0135.png", "0136.png", "0196.png", "0197.png", "0470.png", "0471.png", "0700.png")}]},
)

bears = (
    (
        {"color": evocolor, "tree": ["0759.png", "0760.png"]},
        (
            {"color": evocolor, "tree": ["0674.png", "0675.png"]},
            {"color": humanevocolor, "tree": ["0891.png", {"color": gmaxcolor, "tree": ["0892.png",{"anchor": True, "tree": ("gmaxurshifusingle.png","gmaxurshifurapid.png")}]}]},
        )
    ),
    (
        {"color": evocolor, "tree": ["0446.png", {"color": megacolor, "tree": ["0143.png","gmaxsnorlax.png"]}]},
        (
            {"color": evocolor, "tree": ["0613.png", "0614.png"]},
            {"color": evocolor, "tree": ["0216.png", "0217.png", {"color": changecolor, "tree": ["0901.png","0901_01.png"]}]},
        )
    ),
)

pinnipeds = (
    (
        {"color": evocolor, "tree": ["0728.png", "0729.png", "0730.png"]},
        {"color": evocolor, "tree": ["0086.png", "0087.png"]}
    ),
    {"color": evocolor, "tree": ["0363.png", "0364.png", "0365.png"]},
)

mustelids = (
    {"color": evocolor, "tree": ["0434.png", "0435.png"]},
    (
        "0327.png",
        (
            (
                {"color": variantcolor, "tree": (
                    {"color": evocolor, "tree": ["0263.png","0264.png"]},
                    {"color": evocolor, "tree": ["0263_01.png","0264_01.png", "0862.png"]}
                )},
                {"color": evocolor, "tree": ["0155.png", "0156.png", {"anchor": True, "tree": ("0157.png", {"color": humanevocolor, "tree": "0157_01.png"})}]},
            ),
            (
                (
                    {"color": evocolor, "tree": ["0418.png","0419.png"]},
                    (
                        {"color": evocolor, "tree": ["0619.png","0620.png"]},
                        (
                            {"color": variantcolor, "tree": (
                                {"color": evocolor, "tree": ["0215.png","0461.png"]},
                                {"color": evocolor, "tree": ["0215_01.png","0903.png"]}
                            )},
                        ),
                    ),
                ),
                {"color": evocolor, "tree": ["0501.png", "0502.png", {"anchor": True, "tree": ("0503.png", {"color": humanevocolor, "tree": "0503_01.png"})}]},
            ),
        ),
    )
)

herpestoids = (
    {"color": evocolor, "tree": ["0261.png","0262.png"]},
    (
        "0335.png",
        {"color": evocolor, "tree": ["0734.png","0735.png"]},
    ),
)

cats = (
    (
        {"color": evocolor, "tree": ["0431.png","0432.png"]},
        {"color": evocolor, "tree": ["0300.png","0301.png"]},
    ),
    (
        {"color": megacolor, "tree": ["0359.png","0359_01.png"]},
        (
            (
                {"color": variantcolor, "tree": (
                    (
                        {"color": evocolor, "tree": ["0052_01.png","0053_01.png"]},
                        {"color": evocolor, "tree": ["0052.png",{"anchor": True, "tree": ("0053.png",{"color": gmaxcolor, "tree": "gmaxmeowth.png"})}]},
                    ),
                    {"color": evocolor, "tree": ["0052_02.png","0863.png"]},
                )},
                {"color": evocolor, "tree": ["0509.png","0510.png"]},
            ),
            (
                (
                    (
                        (
                            {"color": evocolor, "tree": ["0667.png",{"anchor": True, "tree": (["0668.png", {"color": megacolor, "colorroot": True, "id": "pyroar-mega", "tree": "0668_02.png"}], {"id": "f-pyroar", "tree": "0668_01.png"})}]},
                            {"color": evocolor, "tree": ["0725.png","0726.png","0727.png"]},
                        ),
                        {"color": evocolor, "tree": ["0403.png","0404.png","0405.png"]},
                    ),
                    {"color": evocolor, "tree": ["0677.png", {"anchor": True, "tree": ("0678.png", "0678_01.png")}]},
                ),
                {"color": evocolor, "tree": ["0906.png","0907.png","0908.png"]},
            ),
        ),
    ),
)
carnivora = (
    (
        canids,
        (
            bears,
            (
                mustelids,
                pinnipeds
            )
        )
    ),
    (
        cats,
        herpestoids,
    ),
)

pangolins = (
    {"color": variantcolor, "tree": (
        {"color": evocolor, "tree": ["0027.png","0028.png"]},
        {"color": evocolor, "tree": ["0027_01.png","0028_01.png"]}
    )},
    {"color": evocolor, "tree": ["0782.png","0783.png","0784.png"]},
)

camels = {"color": evocolor, "tree": ["0322.png", {"color": megacolor, "tree": ["0323.png","0323_01.png"]}]}

pigs = (
    {"color": evocolor, "tree": ["0220.png","0221.png","0473.png"]},
    (
        {"color": evocolor, "tree": ["0325.png","0326.png"]},
        (
            {"color": evocolor, "tree": ["0498.png","0499.png",{"color": megacolor, "tree": ["0500.png","0500_01.png"]}]},
            {"color": evocolor, "tree": ["0915.png",{"anchor": True, "tree": ("0916.png", "0916_01.png")}]},
        ),
    )
)

hipposwhales = (
    (
        {"color": evocolor, "tree": ["0963.png", {"color": formcolor, "tree": ["0964.png","0964_01.png"]}]},
        (
            {"color": evocolor, "tree": ["0320.png","0321.png"]},
            {"color": evocolor, "tree": ["0974.png","0975.png"]},
        )
    ),
    (  
        {"color": evocolor, "tree": ["0293.png","0294.png","0295.png"]},
        {"color": evocolor, "tree": ["0449.png","0450.png"]}, 
    ),
)

ruminants = (
    {"color": evocolor, "tree": ["0203.png","0981.png"]},
    (
        (
            (
                (
                    {"color": evocolor, "tree": ["0672.png","0673.png"]},
                    {"color": gendercolor, "tree": ("0876.png","0876_01.png")},
                ),
                (
                    {"color": evocolor, "tree": ["0831.png","0832.png"]},
                    {"color": evocolor, "tree": ["0179.png", "0180.png", {"color": megacolor, "tree": ["0181.png","0181_01.png"]}]}
                )
            ),
            (
                "0241.png",
                (
                    "0626.png",
                    {"color": variantcolor, "tree": (
                        "0128.png",
                        (
                            "0128_01.png",
                            (
                                "0128_02.png",
                                "0128_03.png"
                            )
                        )
                    )},
                ),
            ),
        ),
        (
            (
                {"color": humanevocolor, "tree": ["0234.png","0899.png"]},
                {"color": evocolor, "tree": [{"id": "springdeerling", "tree": "0585" + sawsbuck + ".png"},{"id": "springsawsbuck", "tree": "0586" + sawsbuck + ".png"}]},
            ),
            (
                "0639.png",
                (
                    "0640.png",
                    "0638.png"
                ),
            ),
        ),
    ),
)

eventoed = (
    camels,
    (
        pigs,
        (
            hipposwhales,
            ruminants
        ),
    ),
)

horses = (
    (
        {"color": deathcolor, "tree": ["0896.png","0897.png"]},
        {"color": evocolor, "tree": ["0749.png","0750.png"]},
    ),
    (
        (
            {"color": evocolor, "tree": ["0522.png","0523.png"]},
            {"color": variantcolor, "tree": (
                {"color": evocolor, "tree": ["0077.png","0078.png"]},
                {"color": evocolor, "tree": ["0077_01.png","0078_01.png"]}
            )},
        ),
        {"color": formcolor, "tree": ["0647.png","0647_01.png"]},
    )
)

tapirsrhinos = (
    (
        {"color": evocolor, "tree": ["0104.png",{"anchor": True, "tree": ("0105.png", "0105_01.png")}]},
        (
            {"color": evocolor, "tree": ["0111.png","0112.png","0464.png"]},
            {"color": gendercolor, "tree": (
                {"color": evocolor, "tree": ["0029.png","0030.png","0031.png"]},
                {"color": evocolor, "tree": ["0032.png","0033.png","0034.png"]}
            )},
        ),
    ),
    (
        {"color": evocolor, "tree": ["0517.png","0518.png"]},
        {"color": evocolor, "tree": ["0096.png","0097.png"]},
    ),
)

oddtoed = (
    horses,
    tapirsrhinos
)

ungulates = (
    oddtoed,
    eventoed
)

bats = (
    (
        {"color": evocolor, "tree": ["0041.png","0042.png","0169.png"]},
        {"color": evocolor, "tree": ["0527.png","0528.png"]},
    ),
    {"color": evocolor, "tree": ["0714.png","0715.png"]},
)

moles = (
    {"color": evocolor, "tree": ["0650.png","0651.png",{"color": megacolor, "tree": ["0652.png","0652_01.png"]}]},
    (
        {"color": variantcolor, "tree": (
            {"color": evocolor, "tree": ["0050.png","0051.png"]},
            {"color": evocolor, "tree": ["0050_01.png","0051_01.png"]}
        )},
        {"color": evocolor, "tree": ["0529.png",{"color": megacolor, "tree": ["0530.png","0530_01.png"]}]},
    ),
)

rabbits = (
    (
        (
            {"color": evocolor, "tree": ["0659.png","0660.png"]},
            {"color": evocolor, "tree": ["0427.png", {"color": megacolor, "tree": ["0428.png","0428_01.png"]}]},
        ),
        {"color": evocolor, "tree": ["0813.png", "0814.png", {"color": gmaxcolor, "tree": ["0815.png","gmaxcinderace.png"]}]},
    ),
    (
        {"color": megacolor, "tree": ["0531.png","0531_01.png"]},
        (
            {"color": evocolor, "tree": ["0298.png","0183.png","0184.png"]},
            {"color": evocolor, "tree": ["0174.png","0039.png","0040.png"]},
        )
    )
)

pikachus = (
    {"color": formcolor, "tree": ["0877.png","0877_01.png"]},
    (
        (
            "0587.png",
            (
                (
                    "0311.png",
                    "0312.png"
                ),
                {"color": evocolor, "tree": ["0921.png","0922.png","0923.png"]},
            )
        ),
        (
            (
                "0417.png",
                {"color": evocolor, "tree": ["0819.png","0820.png"]},
            ),
            (
                "0777.png",
                (
                    "0702.png",
                    {"color": evocolor, "tree": ["0172.png", "0025.png", {"anchor": True, "tree": (
                        ["0026.png",{"anchor": True, "tree": ({"colorroot": True, "color": megacolor, "tree": ("0026_02.png")},{"colorroot": True, "color": megacolor, "tree": ("0026_03.png")})}],
                        "0026_01.png",
                        {"color": gmaxcolor, "tree": "gmaxpikachu.png"},
                        {"color": changecolor, "tree": "0025_08.png"})}]},
                )
            )
        )
    ),
)

mice = (
    (
        pikachus,
        {"color": evocolor, "tree": ["0504.png","0505.png"]},
    ),
    (
        (
            {"color": evocolor, "tree": ["0572.png","0573.png"]},
            {"color": formcolor, "tree": ["0924.png","0925.png"]},
        ),
        (
            {"color": evocolor, "tree": ["0399.png","0400.png"]},
            {"color": variantcolor, "tree": (
                {"color": evocolor, "tree": ["0019.png","0020.png"]},
                {"color": evocolor, "tree": ["0019_01.png","0020_01.png"]}
            )},
        )
    )
)

rodents = (
    rabbits,
    mice
)

humans = (
    {"color": deathcolor, "tree": ["human.png",
        {"anchor": True, "tree":(
            [{"color": megacolor, "tree": [{"id": "glalie", "tree": "0362.png"},"0362_01.png"]}],
            [{"color": megacolor, "tree": [{"id": "froslass", "tree": "0478.png"},"0478_01.png"]}],
            "0802.png",
            "1025.png",
            [{"color": evocolor, "tree": ["0092.png", "0093.png", {"color": megacolor, "tree": ["0094.png",{"anchor": True, "tree": ("0094_01.png",{"color": gmaxcolor, "tree": "gmaxgengar.png"})}]}]}],
            "0442.png",
            [{"color": evocolor, "tree": ["0562.png", {"anchor": True, "tree": ("0563.png",{"color": changecolor, "tree": {"color": evocolor, "tree": ["0562_01.png","0867.png"]}})}]}],
            [{"color": evocolor, "tree": ["0679.png","0680.png","0681.png"]}],
            [{"color": evocolor, "tree": ["0854.png","0855.png"]}],
            [{"color": evocolor, "tree": ["1012.png","1013.png"]}],
            [{"color": evocolor, "tree": ["0935.png",{"anchor": True, "tree": ("0936.png","0937.png")}]}],
            "1001.png",
            "1002.png",
            "1003.png",
            "1004.png",
            [{"color": evocolor, "tree": ["0708.png","0709.png"]}],
            [{"color": evocolor, "tree": ["0710.png","0711.png"]}],
            [{"color": evocolor, "tree": ["0999.png", {"id": "gholdengo", "tree": "1000.png"}]}],
            {"id": "roaminggimmighoul", "tree": "0999_01.png"},
            {"color": createdcolor, "tree": {"color": changecolor, "tree": ["0773.png","0772.png"]}},
            {"color": createdcolor, "tree": {"color": evocolor, "tree": ["0622.png","0623.png"]}},
            {"color": createdcolor, "tree": "0801.png"},
            {"color": createdcolor, "tree": {"color": evocolor, "tree": ["0436.png","0437.png"]}},
            {"color": createdcolor, "id": "claydol", "tree": "0344.png"},
            {"color": createdcolor, "tree": {"color": evocolor, "tree": ["0137.png","0233.png","0474.png"]}},
            {"color": createdcolor, "tree": "0561.png"},
        )}
    ]}
)

humanlike = (
    (
        {"color": evocolor, "tree": ["0439.png",{"anchor": True, "tree": ("0122.png", ["0122_01.png", "0866.png"])}]},
        (
            (
                {"color": evocolor, "tree": ["0238.png","0124.png"]},
                {"color": evocolor, "tree": ["0574.png","0575.png","0576.png"]},
            ),
            (
                (
                    {"color": megacolor, "tree": ["0303.png","0303_01.png"]},
                    {"color": evocolor, "tree": ["0957.png","0958.png","0959.png"]},
                ),
                (
                    {"color": evocolor, "tree": ["0280.png", "0281.png", {"anchor": True, "tree": ({"color": megacolor, "tree": ["0282.png","0282_01.png"]}, {"color": megacolor, "tree": ["0475.png","0475_01.png"]})}]},
                    (
                        {"color": evocolor, "tree": ["0859.png", "0860.png", {"color": gmaxcolor, "tree": ["0861.png","gmaxgrimmsnarl.png"]}]},
                        {"color": evocolor, "tree": ["0856.png", "0857.png", {"color": gmaxcolor, "tree": ["0858.png","gmaxhatterene.png"]}]},
                    )
                )
            )
        )
    ),
    (
        (
            {"color": megacolor, "tree": ["0296.png","0297.png"]},
            {"color": evocolor, "tree": ["0066.png", "0067.png", {"color": gmaxcolor, "tree": ["0068.png","gmaxmachamp.png"]}]},
        ),
        (
            (
                {"color": evocolor, "tree": ["0307.png", {"color": megacolor, "tree": ["0308.png","0308_01.png"]}]},
                {"color": evocolor, "tree": ["0236.png", {"anchor": True, "tree": ("0106.png","0107.png","0237.png")}]},
            ),
            (
                {"color": evocolor, "tree": ["0532.png","0533.png","0534.png"]},
                (
                    (
                        "0538.png",
                        "0539.png"
                    ),
                    humans
                )
            )
        )
    )
)

primates = (
    (
        "0766.png",
        {"color": evocolor, "tree": ["0944.png","0945.png"]},
    ),
    (
        (
            {"color": evocolor, "tree": ["0239.png","0125.png","0466.png"]},
            (
                {"color": evocolor, "tree": ["0390.png","0391.png","0392.png"]},
                (
                    {"color": evocolor, "tree": ["0190.png","0424.png"]},
                    (
                        {"color": evocolor, "tree": ["0511.png","0512.png"]},
                        {"color": evocolor, "tree": ["0513.png","0514.png"]},
                        {"color": evocolor, "tree": ["0515.png","0516.png"]},
                    )
                )
            )
        ),
        (
            (
                (
                    "0893.png",
                    {"color": evocolor, "tree": ["0810.png","0811.png",{"color": gmaxcolor, "tree": ["0812.png","gmaxrillaboom.png"]}]},
                ),
                (
                    {"color": changecolor, "tree": ["mysterymunkidori.png","1015.png"]},
                    (
                        {"color": evocolor, "tree": ["0056.png","0057.png","0979.png"]},
                        {"color": variantcolor, "tree": (
                            {"color": evocolor, "tree": ["0554.png",{"color": formcolor, "tree": ["0555.png","0555_02.png"]}]},
                            {"color": evocolor, "tree": ["0554_01.png",{"color": formcolor, "tree": ["0555_01.png","0555_03.png"]}]}
                        )},
                    )
                )
            ),
            (
                "0765.png",
                humanlike
            )
        )
    )
)

elephantssloths = (
    (
        (
            "0631.png",
            {"color": evocolor, "tree": ["0108.png","0463.png"]},
        ),
        {"color": evocolor, "tree": ["0287.png","0288.png","0289.png"]},
    ),
    (
        {"color": evocolor, "tree": ["0231.png","0232.png"]},
        {"color": evocolor, "tree": ["0878.png","0879.png"]},
    ),
)

marsupials = (
    {"color": megacolor, "tree": ["0115.png","0115_01.png"]},
    "0775.png",
)

monotremes = (
    {"color": evocolor, "tree": ["0270.png","0271.png","0272.png"]},
    {"color": evocolor, "tree": ["0440.png","0113.png","0242.png"]},
)

mammals = (
    monotremes,
    (
        marsupials,
        (
            elephantssloths,
            (
                (
                    moles,
                    (
                        bats,
                        (
                            (
                                carnivora,
                                pangolins
                            ),
                            ungulates
                        ), 
                    ),
                ),
                (
                    rodents,
                    primates
                )
            ),
        ),
    ),
)

lizarddragons = (
    (
        (
            (
                {"color": evocolor, "tree": ["0147.png", "0148.png", {"color": megacolor, "tree": ["0149.png","0149_01.png"]}]},
                {"color": megacolor, "tree": ["0780.png","0780_01.png"]}
            ),
            {"color": evocolor, "tree": ["0840.png", {"anchor": True, "tree": ({"id": "flapple", "tree": "0841.png"}, {"id": "appletun", "tree": "0842.png"}, {"color": humanevocolor, "colorroot": True, "tree": ["1011.png", "1019.png"]})}]},
        ),
        (
            {"color": evocolor, "tree": ["0633.png", "0634.png", "0635.png"]},
            (
                {"color": evocolor, "tree": ["0371.png", "0372.png", {"color": megacolor, "tree": ["0373.png","0373_01.png"]}]},
                (
                    {"color": evocolor, "tree": ["0004.png", "0005.png", {"color": megacolor, "tree": ["0006.png",{"anchor": True, "tree": ("0006_01.png","0006_02.png",{"color": gmaxcolor, "tree": "gmaxcharizard.png"})}]}]},
                    "0621.png"
                )
            )
        ),
    ),
    (
        {"color": evocolor, "tree": ["0252.png", "0253.png", {"color": megacolor, "tree": ["0254.png","0254_01.png"]}]},
        "0967.png"
    )
)

lizards = (
    lizarddragons,
    (
        {"color": evocolor, "tree": ["0559.png", {"color": megacolor, "tree": ["0560.png","0560_01.png"]}]},
        (
            "0352.png",
            (
                (
                    {"color": evocolor, "tree": ["0848.png", {"anchor": True, "tree": ({"id": "ampedtox", "tree": "0849.png"},{"id": "lowkeytox", "tree": "0849_01.png"})}]},
                    {"color": evocolor, "tree": ["0694.png", "0695.png"]},
                ),
                (
                    {"color": evocolor, "tree": ["0757.png", "0758.png"]},
                    {"color": evocolor, "tree": ["0816.png", "0817.png", {"color": gmaxcolor, "tree": ["0818.png","gmaxinteleon.png"]}]},
                )
            )
        )
    )
)

snakes = (
    (
        {"color": evocolor, "tree": ["0206.png", "0982.png"]},
        {"color": evocolor, "tree": ["0495.png", "0496.png", "0497.png"]}
    ),
    (
        {"color": evocolor, "tree": ["0843.png", {"color": gmaxcolor, "tree": ["0844.png","gmaxsandaconda.png"]}]},
        (
            "0336.png",
            {"color": evocolor, "tree": ["0023.png", "0024.png"]},
        )
    )
)

turtles = [
    "0564.png", 

    {"anchor": True, "tree":(
        (
            (
                {"color": evocolor, "tree": ["0007.png", "0008.png", {"color": megacolor, "tree": ["0009.png",{"anchor": True, "tree": ("0009_01.png",{"color": gmaxcolor, "tree": "gmaxblastoise.png"})}]}]},
                (
                    {"color": changecolor, "tree": ["mysteryterapagos.png", {"color": formcolor, "tree": ["1024.png", "1024_01.png",{"color": imbuedcolor, "tree": ["1024_02.png",{"color": evocolor, "tree": ["0969.png","0970.png"]}]}]}]},
                    (
                        "0776.png",
                        "0324.png"
                    ),
                ),
            ),
            {"color": evocolor, "tree": ["0833.png", {"color": gmaxcolor, "tree": ["0834.png","gmaxdrednaw.png"]}]},
        ),
        {"color": evocolor, "tree": "0565.png"},
    )},
]

crocodiles = (
    (
        {"color": evocolor, "tree": ["0158.png", "0159.png", {"color": megacolor, "tree": ["0160.png","0160_01.png"]}]},
        {"color": evocolor, "tree": ["0551.png", "0552.png", "0553.png"]}
    ),
    {"color": evocolor, "tree": ["0909.png", "0910.png", "0911.png"]},
)

flightlessbirds = (
    {"color": evocolor, "tree": ["0084.png", "0085.png"]},
    {"color": evocolor, "tree": ["0955.png", "0956.png"]},
)

ducks = (
    (
        (
            {"color": evocolor, "tree": ["0054.png", "0055.png"]},
            (
                (
                    {"color": evocolor, "tree": ["0240.png","0126.png","0467.png"]},
                    {"color": evocolor, "tree": ["0255.png", "0256.png", {"color": megacolor, "tree": ["0257.png","0257_01.png"]}]},
                ),
                {"color": evocolor, "tree": ["0912.png","0913.png","0914.png"]}
            )
        ),
        {"color": variantcolor, "tree": (
            "0083.png",
            {"color": evocolor, "tree": ["0083_01.png","0865.png"]}
        )},
    ),
    {"color": evocolor, "tree": ["0580.png", "0581.png"]},
)

fairybirds = (
    (
        (
            {"color": humanevocolor, "tree": ["0682.png","0683.png"]},
            (
                "0764.png",
                {"color": formcolor, "tree": ["baseflabebe.png", {"anchor": True, "tree": (["0669" + florges + ".png",{"color": evocolor, "colorroot": True, "tree": ["0670" + florges + ".png","0671" + florges + ".png"]}], ["0669_05.png",{"color": evocolor, "colorroot": True, "tree": {"color": megacolor, "tree": ["0670_05.png","0670_06.png"]}}])}]},
            )
        ),
        {"color": evocolor, "tree": ["0175.png","0176.png","0468.png"]},
    ),
    {"color": changecolor, "tree": ["mysteryfezandipiti.png","1016.png"]},
)

flamingos = "0973.png"

pigeons = {"color": evocolor, "tree": ["0519.png","0520.png","0521.png"]}

penguins = (
    (
        {"color": formcolor, "tree": ["0875_01.png", "0875.png"]},
        "0225.png"
    ),
    {"color": evocolor, "tree": ["0393.png","0394.png","0395.png"]},
)

divingbirds = (
    (
        (
            "0962.png",
            "0845.png"
        ),
        (
            (
                {"color": evocolor, "tree": ["0278.png","0279.png"]},
                {"color": variantcolor, "tree": ("0144.png","0144_01.png")},
            ),
            {"color": evocolor, "tree": ["0940.png","0941.png"]},
        ),
    ),
    {"color": evocolor, "tree": ["0177.png","0178.png"]},
)

owls = (
    {"color": evocolor, "tree": ["0722.png", "0723.png", {"anchor": True, "tree": ("0724.png", {"color": humanevocolor, "tree": "0724_01.png"})}]},
    {"color": evocolor, "tree": ["0163.png","0164.png"]}
)

hawks = (
    (
        (
            {"color": evocolor, "tree": ["0021.png","0022.png"]},
            {"color": megacolor, "tree": ["0227.png","0227_01.png"]},
        ),
        (
            {"color": variantcolor, "tree": ("0145.png","0145_01.png")},
            {"color": evocolor, "tree": ["0627.png", {"anchor": True, "tree": ("0628.png", "0628_01.png")}]},
        ),
    ),
    {"color": evocolor, "tree": ["0629.png","0630.png"]},
)

woodpeckers = {"color": evocolor, "tree": ["0731.png","0732.png","0733.png"]}

songbirds = (
    {"color": evocolor, "tree": ["0198.png","0430.png"]},
    (
        {"color": evocolor, "tree": ["0821.png", "0822.png", {"color": gmaxcolor, "tree": ["0823.png","gmaxcorviknight.png"]}]},
        (
            (
                (
                    {"color": formcolor, "tree": ["0741.png", {"anchor": True, "tree": ({"id": "pompom", "tree": "0741_01.png"}, {"id": "pau", "tree": "0741_02.png"}, {"id": "sensu", "tree": "0741_03.png"})}]},
                    (
                        {"color": variantcolor, "tree": ("0931.png","0931_01.png","0931_02.png","0931_03.png")},
                        "0441.png",
                    )
                ),
                {"color": evocolor, "tree": ["0333.png", {"color": megacolor, "tree": ["0334.png","0334_01.png"]}]},
            ),
            (
                {"color": evocolor, "tree": ["0016.png", "0017.png", {"color": megacolor, "tree": ["0018.png","0018_01.png"]}]},
                (
                    {"color": evocolor, "tree": ["0276.png","0277.png"]},
                    (
                        {"color": evocolor, "tree": ["0396.png","0397.png","0398.png"]},
                        (
                            {"color": evocolor, "tree": ["0661.png","0662.png","0663.png"]},
                            {"color": variantcolor, "tree": ("0146.png","0146_01.png")}
                        )
                    )
                )
            )
        )
    )
)

birds = (
    (
        (
            (
                fairybirds,
                ducks
            ),
            (
                flamingos,
                (
                    pigeons,
                    (
                        (
                            divingbirds,
                            penguins
                        ),
                        (
                            (
                                woodpeckers,
                                (
                                    hawks,
                                    owls
                                ),
                            ),
                            songbirds
                        )
                    )
                )
            )
        ),
        flightlessbirds
    ),
    {"id": "zolt", "tree": "zolt.png"},
)  

dinosaurs = (
    (
        {"color": gmaxcolor, "tree": ["0131.png","gmaxlapras.png"]},
        {"id": "arcto", "tree": "arcto.png"}
    ),
    (
        (
            (
                (
                    (
                        (
                            birds,
                            {"color": evocolor, "tree": ["0566.png", "0567.png"]},
                        ),
                        {"color": megacolor, "tree": ["0701.png", "0701_01.png"]},
                    ),
                    (
                        (
                            {"color": evocolor, "tree": ["0610.png", "0611.png", "0612.png"]},
                            (
                                (
                                    {"color": evocolor, "tree": ["0246.png", "0247.png", {"color": megacolor, "tree": ["0248.png","0248_01.png"]}]},
                                    (
                                        {"color": evocolor, "tree": ["0884.png", {"anchor": True, "tree": ("1018.png",{"color": gmaxcolor, "tree": "gmaxduraludon.png"})}]},
                                        {"color": evocolor, "tree": ["0304.png", "0305.png", {"color": megacolor, "tree": ["0306.png","0306_01.png"]}]},
                                    )
                                ),
                                {"color": evocolor, "tree": ["0996.png", "0997.png", {"color": megacolor, "tree": ["0998.png","0998_01.png"]}]},
                            ),
                        ),
                        {"color": evocolor, "tree": ["0696.png", "0697.png"]},
                    ),
                ),
                (
                    {"color": evocolor, "tree": ["0698.png", "0699.png"]},
                    (
                        (
                            {"color": evocolor, "tree": ["0152.png", "0153.png", {"color": megacolor, "tree": ["0154.png","0154_01.png"]}]},
                            {"color": evocolor, "tree": ["0387.png", "0388.png", "0389.png"]},
                        ),
                        "0357.png",
                    ),
                ),
            ),
            (
                {"id": "draco", "tree": "draco.png"},
                (
                    {"color": evocolor, "tree": ["0410.png", "0411.png"]},
                    {"color": evocolor, "tree": ["0408.png", "0409.png"]}
                ),
            ),
        ),
        {"color": changecolor, "tree": ["0142_01.png", {"color": megacolor, "tree": ["0142.png","0142_01.png"]}]},
    )
)

reptiles = (
    (
        lizards,
        snakes
    ),
    (
        turtles,
        (
            dinosaurs,
            crocodiles
        )
    )
)



amphibians = (
    (
        (
            (
                {"color": evocolor, "tree": ["0453.png","0454.png"]},
                {"color": evocolor, "tree": ["0656.png", "0657.png", {"color": megacolor, "tree": ["0658.png",{"anchor": True, "tree": ("0658_01.png","0658_02.png")}]}]},
            ),
            (
                (
                    {"color": evocolor, "tree": ["0938.png","0939.png"]},
                    {"color": evocolor, "tree": ["0060.png", "0061.png", {"anchor": True, "tree": ("0062.png", "0186.png")}]},
                ),
                {"color": evocolor, "tree": ["0535.png","0536.png","0537.png"]},
            )
        ),
        {"color": evocolor, "tree": ["0001.png", "0002.png", {"color": megacolor, "tree": ["0003.png",{"anchor": True, "tree": ("0003_01.png",{"color": gmaxcolor, "tree": "gmaxvenusaur.png"})}]}]},
    ),
    (
        (
            {"color": evocolor, "tree": ["0258.png", "0259.png", {"color": megacolor, "tree": ["0260.png","0260_01.png"]}]},
            {"color": variantcolor, "tree": (
                {"color": evocolor, "tree": ["0194.png","0195.png"]},
                {"color": evocolor, "tree": ["0194_01.png","0980.png"]}
            )},
        ),
        {"color": variantcolor, "tree": (
            {"color": evocolor, "tree": ["0079.png",{"anchor": True, "tree": ("0199.png", ["0080.png",{"color": megacolor, "colorroot": True, "tree": "0080_01.png"}])}]},
            {"color": humanevocolor, "tree": ["0079_01.png",{"anchor": True, "tree": ("0080_02.png","0199_01.png")}]},
        )},
    ),
)

tetrapods = (
    amphibians,
    (
        {"color": deathcolor, "tree": ["mysterydreepy.png", {"color": evocolor, "tree": ["0885.png", "0886.png", "0887.png"]}]},
        (
            reptiles,
            mammals
        ),
    ),
)

sharks = (
    {"color": evocolor, "tree": ["0458.png","0226.png"]},
    (
        {"color": evocolor, "tree": ["0443.png", "0444.png", {"color": megacolor, "tree": ["0445.png","0445_01.png"]}]},
        {"color": evocolor, "tree": ["0318.png", {"color": megacolor, "tree": ["0319.png","0319_01.png"]}]},
    )
)

eels = (
    {"color": evocolor, "tree": ["0960.png","0961.png"]},
    {"color": evocolor, "tree": ["0366.png",{"anchor": True, "tree": ("0367.png","0368.png")}]}
)

carpsandco = (
    (
        (
            (
                (
                    {"color": evocolor, "tree": ["0349.png","0350.png"]},
                    {"color": evocolor, "tree": ["0129.png", {"color": megacolor, "tree": ["0130.png","0130_01.png"]}]},
                ),
                {"color": variantcolor, "tree": ("0978.png","0978_01.png","0978_02.png")},
            ),
            {"color": evocolor, "tree": ["0118.png","0119.png"]},
        ),
        (
            {"color": evocolor, "tree": ["0602.png","0603.png",{"color": megacolor, "tree": ["0604.png","0604_01.png"]}]},
            (
                {"color": evocolor, "tree": ["0339.png","0340.png"]},
                "0977.png"
            )
        )
    ),
    "0746.png",
)

seahorses = (
    {"color": evocolor, "tree": ["0116.png","0117.png","0230.png"]},
    {"color": evocolor, "tree": ["0690.png",{"color": megacolor, "tree": ["0691.png","0691_01.png"]}]},
)

tetraodonts = (
    "0779.png",
    (
        "0594.png",
        {"color": variantcolor, "tree": (
            "0211.png",
            {"color": evocolor, "tree": ["0211_01.png","0904.png"]},
        )},
    )
)

fish = (
    {"id": "vish", "tree": "vish.png"},
    (
        sharks,
        (
            (
                (
                    carpsandco,
                    (
                        "0976.png",
                        (
                            seahorses,
                            (
                                (
                                    {"color": variantcolor, "tree": ("0618.png","0618_01.png")},
                                    {"color": evocolor, "tree": ["0846.png","0847.png"]},
                                ),
                                (
                                    "0370.png",
                                    (
                                        {"color": variantcolor, "tree": ("0550.png","0550_01.png",{"color": evocolor, "tree": ["0550_02.png",{"anchor": True, "tree": ("0902.png","0902_01.png")}]})},
                                        (
                                            {"color": evocolor, "tree": ["0456.png","0457.png"]},
                                            (
                                                {"color": evocolor, "tree": ["0170.png","0171.png"]},
                                                tetraodonts
                                            )
                                        ),
                                    )
                                )
                            )
                        ),
                    )
                ),
                eels,
            ),
            (
                "0369.png",
                tetrapods
            ),
        )
    )
)

echinoderms = (
    {"color": evocolor, "tree": ["0345.png","0346.png"]},
    (
        (
            "0871.png",
            "0771.png"
        ),
        {"color": evocolor, "tree": ["0747.png","0748.png"]},
    )
)

deuterostomes = (
    echinoderms,
    fish
)

worms = (
    "0968.png",
    {"color": evocolor, "tree": ["0095.png", {"color": megacolor, "tree": ["0208.png","0208_01.png"]}]},
)

cephalopods = ["0138.png", 
    {"anchor": True, "tree":(
        {"color": evocolor, "tree": "0139.png"},
        (
            {"color": evocolor, "tree": ["0686.png", {"color": megacolor, "tree": ["0687.png","0687_01.png"]}]},
            (
                {"color": evocolor, "tree": ["0223.png","0224.png"]},
                {"color": evocolor, "tree": ["0852.png","0853.png"]},
            )
        )
    )}
]

gastropods = (
    {"color": changecolor, "tree": ["0489.png","0490.png"]},
    (
        (
            {"color": variantcolor, "tree": (
                {"color": evocolor, "tree": ["0422.png","0423.png"]},
                {"color": evocolor, "tree": ["0422_01.png","0423_01.png"]},
            )},
            (
                {"color": humanevocolor, "tree": ["0616.png","0617.png"]},
                (
                    "mussel.png",
                    {"color": evocolor, "tree": ["0090.png","0091.png"]},
                )
            ),
        ),
        (
            (
                {"color": evocolor, "tree": ["0316.png","0317.png"]},
                {"color": evocolor, "tree": ["0704.png",{"anchor": True, "tree": (["0705.png", "0706.png"], ["0705_01.png", "0706_01.png"])}]},
            )
        )
    )
)

molluscs = (
    cephalopods,
    gastropods
)

arachnids = (
    (
        (
            {"color": evocolor, "tree": ["0451.png","0452.png"]},
            {"color": evocolor, "tree": ["0207.png","0472.png"]},
        ),
        (
            {"color": evocolor, "tree": ["0751.png","0752.png"]},
            (
                (
                    {"color": evocolor, "tree": ["0167.png","0168.png"]},
                    {"color": evocolor, "tree": ["0917.png","0918.png"]},
                ),
                {"color": evocolor, "tree": ["0595.png","0596.png"]},
            )
        )
    ),
    {"color": evocolor, "tree": ["0140.png","0141.png"]},
)

centipedes = (
    {"color": evocolor, "tree": ["0850.png",{"color": gmaxcolor, "tree": ["0851.png","gmaxcentiskorch.png"]}]},
    {"color": evocolor, "tree": ["0543.png","0544.png",{"color": megacolor, "tree": ["0545.png","0545_01.png"]}]},
)

crustaceans = (
    {"color": evocolor, "tree": ["0688.png",{"color": megacolor, "tree": ["0689.png","0689_01.png"]}]},
    (
        (
            {"color": evocolor, "tree": ["0692.png","0693.png"]},
            (
                (
                    {"color": evocolor, "tree": ["0098.png",{"color": gmaxcolor, "tree": ["0099.png","gmaxkingler.png"]}]},
                    (
                        {"color": evocolor, "tree": ["0739.png","0740.png"]},
                        "0950.png",
                    )
                ),
                {"color": evocolor, "tree": ["0341.png","0342.png"]},
            )
        ),
        (
            ["0347.png", 
                {"anchor": True, "tree":(
                    (
                        {"color": evocolor, "tree": ["0767.png","0768.png"]},
                        (
                            {"color": evocolor, "tree": ["0046.png","0047.png"]},
                            {"color": evocolor, "tree": ["0557.png","0558.png"]},
                        ),
                    ),
                    {"color": evocolor, "tree": "0348.png"},
                )}
            ]
        ),
    )
)

dragonflies = {"color": evocolor, "tree": ["0193.png","0469.png"]}

cricketsmantises = (
    (
        {"color": evocolor, "tree": ["0123.png", {"anchor": True, "tree": ("0900.png", {"color": humanevocolor, "tree": ["0212.png",{"color": megacolor, "colorroot": True, "tree": "0212_01.png"}]})}]},
        {"color": changecolor, "tree": ["mysterygenesect.png","0649.png"]},
    ),
    (
        {"color": evocolor, "tree": ["0401.png","0402.png"]},
        {"color": evocolor, "tree": ["0919.png","0920.png"]}
    )
)

beesants = (
    (
        "0632.png",
        {"color": evocolor, "tree": ["0540.png","0541.png","0542.png"]},
    ),
    (
        {"color": evocolor, "tree": ["0415.png","0416.png"]},
        {"color": evocolor, "tree": ["0013.png","0014.png",{"color": megacolor, "tree": ["0015.png","0015_01.png"]}]},
    ),
)

beetles = (
    (
        (
            (
                {"color": megacolor, "tree": ["0127.png","0127_01.png"]},
                {"color": evocolor, "tree": ["0736.png","0737.png","0738.png"]}
            ),
            (
                {"color": megacolor, "tree": ["0214.png","0214_01.png"]},
                (
                    (
                        {"color": evocolor, "tree": ["0624.png","0625.png","0983.png"]},
                        {"color": megacolor, "tree": ["0870.png","0870_01.png"]}
                    ),
                    {"color": humanevocolor, "tree": ["0588.png","0589.png"]},
                ),
            ),
        ),
        (
            {"color": evocolor, "tree": ["0953.png","0954.png"]},
            (
                (
                    {"color": evocolor, "tree": ["0165.png","0166.png"]},
                    {"color": evocolor, "tree": ["0824.png","0825.png",{"color": gmaxcolor, "tree": ["0826.png","gmaxorbeetle.png"]}]},
                ),
                {"color": gendercolor, "tree": ("0313.png","0314.png")},
            )
        )
    ),
    {"color": evocolor, "tree": ["0328.png","0329.png","0330.png"]},
)

truebugs = {"color": evocolor, "tree": ["0290.png",{"anchor": True, "tree": ("0291.png", {"color": splitcolor, "tree": "0292.png"})}]}

moths = (
    {"color": evocolor, "tree": ["0742.png","0743.png"]},
    (
        {"color": evocolor, "tree": ["0283.png","0284.png"]},
        (
            {"color": evocolor, "tree": ["0048.png","0049.png"]},
            (
                (
                    {"color": evocolor, "tree": ["0636.png","0637.png"]},
                    {"color": evocolor, "tree": ["0872.png","0873.png"]},
                ),
                (
                    (
                        {"color": evocolor, "tree": ["0204.png","0205.png"]},
                        {"color": formcolor, "tree": ["nocloakburmy.png", {"anchor": True, "tree": ({"id": "plantcloak", "tree": ["0412.png",{"color": evocolor, "colorroot": True, "tree": "0413.png"}]}, {"id": "sandcloak", "tree": ["0412_01.png",{"color": evocolor, "colorroot": True, "tree": "0413_01.png"}]}, {"id": "trashcloak", "tree": ["0412_02.png",{"color": evocolor, "colorroot": True, "tree": "0413_02.png"}]})}]},
                    ),
                    (
                        {"color": evocolor, "tree": ["0010.png","0011.png",{"color": gmaxcolor, "tree": ["0012.png","gmaxbutterfree.png"]}]},
                        (
                            {"color": evocolor, "tree": ["0664.png","0665.png","0666" + vivillon + ".png"]},
                            {"color": evocolor, "tree": ["0265.png", {"anchor": True, "tree": (["0266.png","0267.png"], ["0268.png","0269.png"])}]},
                        ),
                    )
                ),
            ),
        ),
    ),
)

insects = (
    dragonflies,
    (
        (
            truebugs,
            (
                (
                    beetles,
                    moths
                ),
                beesants
            )
        ),
        cricketsmantises
    )
)

arthropods = (
    arachnids,
    (   
        centipedes,
        (
            crustaceans,
            insects
        ),
    )
)

protostomes = (
    (
        (
            molluscs,
            worms
        ),
        {"color": evocolor, "tree": ["0360.png","0202.png"]},
    ),
    arthropods
)

cnidarians = (
    (
        {"color": evocolor, "tree": ["0592.png","0593.png"]},
        {"color": evocolor, "tree": ["0072.png","0073.png"]}
    ),
    (
        "coral.png",
        {"color": variantcolor, "tree": (
            "0222.png",
            {"color": deathcolor, "tree": ["mysterygorsola.png", {"color": evocolor, "tree": ["0222_01.png","0864.png"]}]}
        )},
    )
)

animals = [{"id": "mew", "tree": "0151.png"}, 
    {"anchor": True, "tree": (
        {"color": changecolor, "id": "mewtwo", "tree": ["0150.png",
            {"anchor": True, "tree": ({"colorroot": True, "color": megacolor, "tree": ("0150_01.png")},
            {"colorroot": True, "color": megacolor, "tree": ("0150_02.png")})}
        ]},
        (
            cnidarians,
            (
                protostomes,
                deuterostomes
            )
        )
    )}
]

fungus = (
    (
        (
            {"color": evocolor, "tree": ["0948.png","0949.png"]},
            "ironbarktongue.png"
        ),
        (
            (
                (
                    (
                        (
                            {"color": evocolor, "tree": ["0285.png","0286.png"]},
                            (
                                "balmmushroom.png",
                                "roundmushroom.png"
                            )
                        ),
                        (
                            (
                                "springymushroom.png",
                                "maxmushroom.png"
                            ),
                            (
                                {"color": evocolor, "tree": ["0590.png","0591.png"]},
                                (
                                    {"color": evocolor, "tree": ["0755.png","0756.png"]},
                                    {"color": formcolor, "tree": ["tinymushroom.png","bigmushroom.png"]},
                                )
                            )
                        )
                    ),
                    "doppelbonnet.png",
                ),
                "direshroom.png"
            ),
            "swordcap.png",
        )
    ),
    "truffle.png"
)

algae = (
    {"color": deathcolor, "tree": ["mysterydhelmise.png","0781.png"]},
    "poppod.png"
)

moss = "luminousmoss.png"

ferns = "casterfern.png"

gymnosperms = {"color": evocolor, "tree": ["0459.png",{"color": megacolor, "tree": ["0460.png","0460_01.png"]}]}

lilypads = "lotadlilypad.png"

magnoliids = (
    "blackpepper.png",
    (
        (
            "cinnamon.png",
            "avocado.png"
        ),
        "galarica.png"
    ),
)

monocots = (
    (
        (
            {"color": evocolor, "tree": ["0548.png", {"anchor": True, "tree": ("0549.png", "0549_01.png")}]},
            {"color": variantcolor, "tree": ("lonelyflower.png","lovelyflower.png")}
        ),
        "eternalflower.png"
    ),
    (
        (
            (
                "blueflower.png",
                (
                    (
                        {"color": variantcolor, "tree": (("scallion.png","medicinalscallion.png"),"largescallion.png")},
                        {"color": variantcolor, "tree": ("redonion.png","whiteonion.png")},
                    ),
                    "absorbbulb.png"
                )
            ),
            {"color": evocolor, "tree": ["0753.png","0754.png"]},
        ),
        (
            (
                (
                    (
                        {"color": formcolor, "tree": ["tinybamboo.png","bigbamboo.png"]},
                        (
                            "tallgrass.png",
                            "heartygrains.png",
                        )
                    ),
                    "rice.png"
                ),
                "pineapple.png",
            ),
            (
                (
                    "banana.png",
                    {"color": variantcolor, "tree": ({"color": formcolor, "tree": ["energyroot.png","bigroot.png"]},"revivalherb.png")},
                ),
                (
                    {"color": evocolor, "tree": ["0102.png", {"anchor": True, "tree": ("0103.png", "0103_01.png")}]},
                    (
                        "palm.png",
                        "tropicalplant.png"
                    ),
                )
            )
        )
    )
)

small = (
    "leppa.png",
    "cheri.png"
)

oranfamily = (
    "aspear.png",
    (
        small,
        (
            (
                "pecha.png",
                "rawst.png"
            ),
            (
                "oran.png",
                "sitrus.png"
            )   
        )      
    ),
)

drupelets = (
    "bluk.png",
    (
        "babiri.png",
        "razz.png"
    )
)

clusters = (
    "roseli.png",
    (
        "kasib.png",
        "nanab.png"
    )
)

multihusk = (
    "wacan.png",
    (
        "pamtre.png",
        "passho.png"
    )
)

rotational = (
    "chilan.png",
    "occa.png"
)

floral = (
    "hopo.png",
    (
        "lum.png",
        "tanga.png"
    )
)

segmented = (
    (
        "rindo.png",
        drupelets
    ),
    (
        "pinap.png",
        "charti.png"
    )
)

biglumpy = (
    (
        (
            "chople.png",
            (
                (
                    clusters,
                    segmented
                ),
                "persim.png",
            )
        ),
        "figy.png",
    ),
    (
        "iapapa.png",
        (
            "payapa.png",
            "mago.png"
        ),
    ),
)

biground = (
    
    (
        (
            "colbur.png",
            "wiki.png"
        ),
        (
            biglumpy,
            "shuca.png"
        )
    ),
    (
        (
            (
                "wepear.png",
                "aguav.png",
            ),
            (
                "yache.png",
                oranfamily,
            )
        ),
        (
            "haban.png",
            (
                rotational,
                floral,
            )
        )
    )
)

berries = (
    "chesto.png",
    (
        (
            biground,
            multihusk,
        ),
        (
            "kebia.png",
            "passimianberry.png",
        ),
    )
)



fabids = (
    (
        (
            "venusaurflower.png",
            {"color": evocolor, "tree": ["0043.png", "0044.png", {"anchor": True, "tree": ("0045.png", "0182.png")}]},
        ),
        {"color": evocolor, "tree": ["0761.png","0762.png","0763.png"]},
    ),
    (
        (
            (
                (
                    {"color": variantcolor, "tree": ("pokebean.png","plumpbean.png")},
                    "tofu.png",
                ),
                "redbean.png"
            ),
            "peanut.png"
        ),
        (
            (
                (
                    (
                        {"color": evocolor, "tree": ["0420.png",{"color": formcolor, "tree": ["0421.png","0421_01.png"]}]},
                        (
                            "peach.png",
                            "chineseplum.png"
                        )
                    ),
                    {"color": variantcolor, "tree": ("tartapple.png", ("sweetapple.png","fancyapple.png"))},
                ),
                (
                    "strawberry.png",
                    (
                        {"color": evocolor, "tree": ["0406.png","0315.png","0407.png"]},
                        "rose.png"
                    )
                )
            ),
            (
                (
                    "bittermelon.png",
                    (
                        "pumpkaboopumpkin.png",
                        "cucumber.png"
                    )
                ),
                (
                    "phantumpstump.png",
                    (
                        "torterratree.png",
                        (
                            (
                                (
                                    (
                                        (
                                            {"color": variantcolor, "tree": (
                                                {"color": evocolor, "tree": ["0100.png","0101.png"]},
                                                {"color": evocolor, "tree": ["0100_01.png","0101_01.png"]},
                                            )},
                                            "apricorn.png"
                                        ),
                                        berries
                                    )
                                ),
                                (
                                    "pottedplant.png",
                                    {"color": variantcolor, "tree": (
                                        "bigplant.png",
                                        (
                                            "elegantbonsai.png",
                                            "bonsai.png"
                                        )
                                    )}
                                )
                            ),
                            {"color": evocolor, "tree": ["0273.png","0274.png","0275.png"]},
                        )
                    )
                )
            )
        )
    )
)

malvids = (
    "komalalog.png",
    (
        (
            "shinyleaf.png",
            (
                (
                    "lemon.png",
                    (
                        {"color": changecolor, "tree": ["mysteryogerpon.png", {"color": formcolor, "tree": ["1017.png", {"anchor": True, "tree": ("1017_01.png","1017_02.png","1017_03.png")}]}]},
                        "marmalade.png"
                    ),
                    "lime.png"
                ),
                "mango.png"
            )
        ),
        (
            (
                (
                    (
                        {"color": evocolor, "tree": ["0546.png","0547.png"]},
                        {"color": evocolor, "tree": ["0829.png","0830.png"]},
                    ),
                    "sweetheart.png"
                ),
                (
                    "gracidea.png",
                    {"color": variantcolor, "tree": (
                        "redflower.png",
                        "redflowerbase.png"
                    )}
                )
            ),
            (
                {"color": variantcolor, "tree": ("pungentroot.png","pepupplant.png")},
                (
                    (
                        "watercress.png",
                        "horseradish.png"
                    ),
                    (
                        "radish.png",
                        (
                            (
                                "rapeseed.png",
                                (
                                    {"color": variantcolor, "tree": ("broccoli.png","brusselssprout.png")},
                                    "mustard.png"
                                )
                            ),
                            "turnip.png"
                        )
                    )
                )
            )
        )
    )
)

rosids = (
    "grapes.png",
    (
        fabids,
        malvids
    )
)

caryophyllales = (
    (
        "0455.png",
        {"color": evocolor, "tree": ["0069.png", "0070.png", {"color": megacolor, "tree": ["0071.png","0071_01.png"]}]},
    ),
    (
        "spinach.png",
        (
            (
                "0556.png",
                {"color": evocolor, "tree": ["0331.png","0332.png"]},
            ),
            (
                {"color": evocolor, "tree": ["0114.png","0465.png"]},
                "mysterybramblin.png",
            )
        )
    )
)

asterids = (
    (
        (
            (
                (
                    (
                        "lettuce.png",
                        "mirrorherb.png"
                    ),
                    {"color": evocolor, "tree": ["0187.png","0188.png","0189.png"]},
                ),
                (
                    (
                        "stickybarb.png",
                        {"color": evocolor, "tree": ["0597.png","0598.png"]},
                    ),
                    (
                        (
                            (
                                (
                                    {"color": variantcolor, "tree":
                                    (
                                        "pokeflower.png",
                                        "prettyflower.png",
                                        "daintyflower.png",
                                        "colorfulplant.png",
                                        "lavishflower.png"
                                    )},
                                    "gorgeousflower.png",
                                ),
                                "floweringplant.png",
                            ),
                            {"color": evocolor, "tree": ["0191.png","0192.png"]},
                        ),
                        "vivichoke.png"
                    )
                ),
            ),
            (
                "dill.png",
                {"color": variantcolor, "tree": ("carrot.png", ("shaderootcarrot.png", "icerootcarrot.png"))},   
            )         
        ),
        (
            "comfeyflower.png",
            (
                "coffee.png",
                (
                    (
                        (
                            (
                                {"color": evocolor, "tree": ["0928.png","0929.png","0930.png"]},
                                "olive.png"
                            ),
                            "fairyflower.png"
                        ),
                        (
                            (
                                "herbamystica.png",
                                "mint.png"
                            ),
                            (
                                (
                                    "rosemary.png",
                                    (
                                        "lavender.png",
                                        "bugwort.png"
                                    ),
                                ),
                                (
                                    "basil.png",
                                    {"color": variantcolor, "tree": (("whiteherb.png","mentalherb.png"),("kingsleaf.png","powerherb.png"))},
                                )
                            ),
                        )
                    ),
                    (
                        (
                            (
                                "sootfootroot.png",
                                "potato.png"
                            ),
                            (
                                {"color": variantcolor, "tree": ("tomato.png", "cherrytomato.png")},
                                "eggplant.png"
                            )
                        ),
                        (
                            (
                                "chilipepper.png",
                                {"color": evocolor, "tree": ["0951.png","0952.png"]},
                            ),
                            {"color": variantcolor, "tree": ("jalapeno.png", ("redbellpepper.png","yellowbellpepper.png","greenbellpepper.png"))},
                        )
                    )
                )
            )
        )
    ),
    (
        "tea.png",
        (
            "kiwi.png",
            "blueberry.png"
        )
    )
)

eudicots = (
    (
        (
            asterids,
            caryophyllales
        ),
        rosids
    ),
    "poppy.png",
)

plants = (
    algae,
    (
        (
            ferns,
            (
                (
                    lilypads,
                    (
                        (
                            monocots,
                            eudicots
                        ),
                        magnoliids
                    )
                ),
                gymnosperms,
            )
        ),
        moss
    )
)

protists = (
    {"color": evocolor, "tree": ["0577.png","0578.png","0579.png"]},
    "0213.png",
)

viruses = "pokerus.png"

harmonia = {"color": splitcolor, "tree": ["harmonia.png",
    {"anchor": True, "tree": (
        ["0643.png",{"id": "whitekyurem", "color": formcolor, "colorroot": True, "tree": "0646_01.png"}],
        ["0644.png",{"id": "blackkyurem", "color": formcolor, "colorroot": True, "tree": "0646_02.png"}],
        {"id": "kyurem", "tree": "0646.png"},
        {"color": unknowncolor, "colorroot": True, "tree": (
            (
                "0132.png",
                {"color": splitcolor, "tree": ["0809.png",{"anchor": True, "tree": ("0808.png", {"color": gmaxcolor, "colorroot": True, "tree": "gmaxmelmetal.png"})}]},
            ),
            {"color": evocolor, "tree": ["0374.png", "0375.png", {"color": megacolor, "tree": ["0376.png",{"id": "megametagross", "tree": "0376_01.png"}]}]},
        )}
    )}
]}

abiologicalearth = (
    {"color": megacolor, "tree": [{"id": "banette", "tree": "0354.png"},"0354_01.png"]},
    {"color": formcolor, "tree": ["0479.png",{"anchor": True, "tree": ("0479_01.png","0479_02.png","0479_03.png","0479_04.png","0479_05.png")}]},
    {"color": evocolor, "tree": ["0109.png",{"anchor": True, "tree": ("0110.png","0110_01.png")}]},
    {"color": evocolor, "tree": ["0568.png","0569.png"]},
    {"color": evocolor, "tree": ["0965.png","0966.png"]},
    {"color": evocolor, "tree": ["0433.png",{"color": megacolor, "tree": ["0358.png","0358_01.png"]}]},
    "0707.png",
    {"color": evocolor, "tree": ["0599.png","0600.png","0601.png"]},
    "0485.png",
    {"color": evocolor, "tree": ["0218.png","0219.png"]},
    {"color": evocolor, "tree": ["0837.png","0838.png",{"color": gmaxcolor, "tree": ["0839.png","gmaxcoalossal.png"]}]},
    {"color": evocolor, "tree": ["0524.png","0525.png","0526.png"]},
    {"color": changecolor, "tree": ["0703.png", {"color": megacolor, "tree": ["0719.png","0719_01.png"]}]},
    {"color": evocolor, "tree": ["0074.png","0075.png","0076.png"]},
    {"color": evocolor, "tree": ["0074_01.png","0075_01.png","0076_01.png"]},
    {"color": evocolor, "tree": ["0932.png","0933.png","0934.png"]},
    {"color": evocolor, "tree": ["0299.png","0476.png"]},
    {"color": evocolor, "tree": ["0438.png","0185.png"]},
    {"color": evocolor, "tree": ["0712.png",{"anchor": True, "tree": ("0713.png","0713_01.png")}]},
    {"color": evocolor, "tree": ["0582.png","0583.png","0584.png"]},
    "0615.png",
    "0351.png",
    {"color": evocolor, "tree": ["0868.png",{"color": gmaxcolor, "tree": ["0869.png","gmaxalcremie.png"]}]},
    (
        {"color": formcolor, "tree": ["0382.png","0382_01.png"]},
        {"color": formcolor, "tree": ["0383.png","0383_01.png"]},
        {"color": megacolor, "tree": ["0384.png",{"id": "megarayquaza", "tree": "0384_01.png"}]},
        "0807.png",
        "0721.png",
        (
            "0251.png",
            "0898.png"
        ),
        "0249.png",
        "0250.png",
        "0494.png",
        {"color": formcolor, "tree": ["0648.png","0648_01.png"]},

    ),
    (
        "0785.png",
        "0786.png",
        "0787.png",
        "0788.png"
    )
),

abiologicalmoon = (
    "0337.png",
    (
        {"color": unknowncolor, "tree": ["0488.png", {"id": "dreamworld", "tree": (
            {"color": gendercolor, "tree": (
                {"color": megacolor, "tree": ["0380.png","0380_01.png"]},
                {"color": megacolor, "tree": ["0381.png","0381_01.png"]},
            )},
            (
                {"color": formcolor, "tree": ["0641_01.png","0641.png"]},
                {"color": formcolor, "tree": ["0642_01.png","0642.png"]},
                {"color": formcolor, "tree": ["0645_01.png","0645.png"]},
                {"color": formcolor, "tree": ["0905_01.png","0905.png"]},
            )
        )}]},
        {"id": "darkrai", "tree": "0491.png"}
    ),
    {"color": evocolor, "tree": ["0088.png",{"anchor": True, "tree": (
        "0089.png",
        {"color": changecolor, "colorroot": True, "tree": {"color": evocolor, "tree": ["0088_01.png","0089_01.png"]},}
    )}]},
),
    


standaloneabiological = {"color": imbuedcolor, "tree": [
    "laketrio.png",
    {"anchor": True, "tree": (
        abiologicalearth,
        abiologicalmoon,
        "0338.png",
        "0774.png",
        ["0081.png", {"color": evocolor, "colorroot": True, "tree": ["0082.png","0462.png"]}],
        ["0120.png", {"color": evocolor, "colorroot": True, "tree": {"color": megacolor, "tree": ["0121.png","0121_01.png"]}}],
        "0385.png",
    )}
]}


life = (
    (
        protists,
        viruses
    ),
    (
        {"color": formcolor, "tree": ["0492.png","0492_01.png"]},
        (
            (
                fungus,
                plants
            ),
            animals
        )
    )
)

base = {"color": splitcolor, "tree": ["originalone.png",
    {"anchor": True, "tree": (
        ["0487.png",{"colorroot": True, "color": formcolor, "tree": ("0487_01.png")}],
        ["0484.png",{"colorroot": True, "color": formcolor, "tree": ("0484_01.png")}],
        ["0483.png",{"colorroot": True, "color": formcolor, "tree": ("0483_01.png")}],
        "0493.png",
        {"color": unknowncolor, "colorroot": True, "tree": ("0201.png")},
        {"color": createdcolor, "colorroot": True, "tree": {"color": imbuedcolor, "tree": [
            "laketrio.png",
            {"anchor": True, "tree": (
                abiologicalearth,
                abiologicalmoon,
                "0338.png",
                "0774.png",
                ["0081.png", {"color": evocolor, "colorroot": True, "tree": ["0082.png","0462.png"]}],
                ["0120.png", {"color": evocolor, "colorroot": True, "tree": {"color": megacolor, "tree": ["0121.png","0121_01.png"]}}],
                "0385.png",
                {"color": createdcolor, "tree": harmonia},
                {"color": createdcolor, "tree": {"color": gmaxcolor, "tree": ["0890.png", {"anchor": True, "tree": (
                    "eternamax.png",
                    {"color": imbuedcolor, "colorroot": True, "tree": "0874.png"}
                )}]}},
                {"color": createdcolor, "tree": [
                    {"id": "regigigas", "tree": "0486.png"},
                    {"anchor": True, "tree": (
                        "0377.png",
                        "0378.png",
                        "0379.png",
                        "0894.png",
                        "0895.png"
                    )},
                ]},
                {"color": createdcolor, "tree": [
                    "treeoflife.png",
                    {"anchor": True, "tree": (
                            {"color": createdcolor, "tree": {"color": changecolor, "tree": ["mysterydeoxys.png", "0386.png",
                                {"anchor": True, "tree": (
                                    {"color": formcolor, "colorroot": True, "tree": "0386_01.png"},
                                    {"color": formcolor, "colorroot": True, "tree": "0386_02.png"},
                                    {"color": formcolor, "colorroot": True, "tree": "0386_03.png"},
                                )}
                            ]}},
                            {"color": createdcolor, "tree": {"color": evocolor, "tree": ["0605.png", "0606.png"]}},
                            {"color": createdcolor, "tree": {"color": evocolor, "tree": ["0173.png", "0035.png", {"color": megacolor, "tree": ["0036.png","0036_01.png"]}]}},
                            {"color": incarnatescolor, "tree": ("0716.png")},
                            {"color": incarnatescolor, "tree": ["0717.png", {"color": unknowncolor, "colorroot": True, "tree": (
                                (
                                    {"color": megacolor, "tree": ["0302.png","0302_01.png"]},
                                    "0778.png"
                                ),
                                (
                                    {"color": evocolor, "tree": ["0355.png","0356.png","0477.png"]},
                                    {"color": evocolor, "tree": ["0607.png","0608.png",{"color": megacolor, "tree": ["0609.png","0609_01.png"]}]},
                                )
                            )}]},
                            {"color": createdcolor, "tree": {"color": splitcolor, "tree": ["0718_04.png", {"anchor": True, "tree": (
                                "0718.png",
                                "0718_01.png",
                                {"color": megacolor, "tree": "0718_03.png"},
                                "zygardecell.png",
                                "zygardecore.png"
                            )}]}},
                            {"color": createdcolor, "tree": {"color": "#000000", "tree": life}},
                    )}
                ]},
            )}
        ]}}
    )}
]}

addmammals = [
    {"new": "hisuizoroark", "roots": ["zoroark"], "color": deathcolor},
    {"new": "0971.png", "id": "greavard", "roots": ["maschiff"], "color": "#ffffff"},
    {"new": "0972.png", "id": "houndstone", "roots": ["greavard"], "color": evocolor},
    {"new": "gholdengo", "roots": ["roaminggimmighoul"], "color": evocolor},
    {"new": "0361.png", "id": "snorunt", "roots": [], "color": evocolor},
    {"new": "glalie", "roots": ["snorunt"], "color": evocolor},
    {"new": "froslass", "roots": ["snorunt"], "color": evocolor},
    {"new": "0343.png", "id": "baltoy", "roots": [], "color": evocolor},
    {"new": "claydol", "roots": ["baltoy"], "color": evocolor},
    {"new": "pyroar-mega", "roots": ["f-pyroar"], "color": megacolor},
]

addbirds = [
    {"new": "sensu", "roots": ["pompom","pau"], "color": formcolor, "dontaffectvert": True,},
    {"new": "pau", "roots": ["pompom"], "color": formcolor, "dontaffectvert": True,},
]

addreptiles = [
    {"new": "gmaxtoxtricity.png", "roots": ["ampedtox", "lowkeytox"], "color": gmaxcolor},
    {"new": "gmaxapple.png", "roots": ["flapple", "appletun"], "color": gmaxcolor},
    #{"new": "0880.png", "id": "dracozolt", "roots": ["draco"], "color": changecolor},
    #{"new": "0881.png", "id": "arctozolt", "roots": ["arcto"], "color": changecolor},
    #{"new": "zolt", "roots": ["dracozolt","arctozolt"], "color": changecolor},
] + addbirds

addfish = [
    #{"new": "0882.png", "id": "dracovish", "roots": ["vish"], "color": changecolor},
    #{"new": "0883.png", "id": "arctovish", "roots": ["vish"], "color": changecolor},
    #{"new": "draco", "roots": ["dracovish"], "color": changecolor},
    #{"new": "arcto", "roots": ["arctovish"], "color": changecolor},
] + addmammals + addreptiles

addbugs = [
    {"new": "0414.png", "id": "mothim", "roots": ["sandcloak"], "color": evocolor},
    {"new": "mothim", "roots": ["plantcloak", "trashcloak"], "color": evocolor, "dontaffectvert": True},
    {"new": "sandcloak", "roots": ["plantcloak", "trashcloak"], "color": formcolor, "dontaffectvert": True},
    #{"new": "plantcloak", "roots": ["trashcloak"], "color": formcolor, "dontaffectvert": True},
]

addanimals = [
    {"new": "0946.png", "dontaffectvert": True, "id": "bramblin", "roots": [], "color": "#ffffff"},
    {"new": "0947.png", "id": "brambleghast", "roots": ["bramblin"], "color": evocolor},
    {"new": "0200.png", "dontaffectvert": True, "id": "misdreavus", "roots": [], "color": "#ffffff"},
    {"new": "0429.png", "id": "mismagius", "roots": ["misdreavus"], "color": evocolor},
    {"new": "0425.png", "dontaffectvert": True, "id": "drifloon", "roots": [], "color": "#ffffff"},
    {"new": "0426.png", "id": "drifblim", "roots": ["drifloon"], "color": evocolor},
    {"new": "0769.png", "dontaffectvert": True, "id": "sandygast", "roots": [], "color": "#ffffff"},
    {"new": "0770.png", "id": "palossand", "roots": ["sandygast"], "color": evocolor},
] + addbugs + addfish

addabiological = [
    {"new": "0353.png", "id": "shuppet", "roots": [], "color": evocolor},
    {"new": "banette", "roots": ["shuppet"], "color": evocolor},
]

multiverse = [
    {"new": "ultrawormhole.png", "id": "wormhole", "roots": ["megarayquaza"], "color": "#ffffff"},
    {"new": "0720_01.png", "id": "hoopaunbound", "roots": ["wormhole"], "color": wormholecolor},
    {"new": "0720.png", "id": "hoopa", "roots": ["hoopaunbound"], "color": changecolor},
    {"new": "0793.png", "id": "nihilego", "roots": ["wormhole"], "color": wormholecolor},
    {"new": "0794.png", "id": "buzzwole", "roots": ["wormhole"], "color": wormholecolor},
    {"new": "0795.png", "id": "pheromosa", "roots": ["wormhole"], "color": wormholecolor},
    {"new": "0796.png", "id": "xurkitree", "roots": ["wormhole"], "color": wormholecolor},
    {"new": "0797.png", "id": "celesteela", "roots": ["wormhole"], "color": wormholecolor},
    {"new": "0798.png", "id": "kartana", "roots": ["wormhole"], "color": wormholecolor},
    {"new": "0799.png", "id": "guzzlord", "roots": ["wormhole"], "color": wormholecolor},
    {"new": "0805.png", "id": "stakataka", "roots": ["wormhole"], "color": wormholecolor},
    {"new": "0806.png", "id": "blacephalon", "roots": ["wormhole"], "color": wormholecolor},
    {"new": "0803.png", "id": "poipole", "roots": ["wormhole"], "color": wormholecolor},
    {"new": "0804.png", "id": "naganadel", "roots": ["poipole"], "color": evocolor},
    {"new": "0789.png", "id": "cosmog", "roots": ["wormhole"], "color": wormholecolor},
    {"new": "0790.png", "id": "cosmoem", "roots": ["cosmog"], "color": evocolor},
    {"new": "0791.png", "id": "solgaleo", "roots": ["cosmoem"], "color": evocolor},
    {"new": "0792.png", "id": "lunala", "roots": ["cosmoem"], "color": evocolor},
    {"new": "0800_03.png", "id": "realnecrozma", "roots": ["wormhole"], "color": wormholecolor},
    {"new": "cosmog", "roots": ["realnecrozma"], "color": unknowncolor},
    {"new": "0800.png", "id": "necrozma", "roots": ["realnecrozma"], "color": changecolor},
    {"new": "0800_01.png", "id": "duskmane", "roots": ["necrozma","solgaleo"], "color": formcolor},
    {"new": "0800_02.png", "id": "dawnwings", "roots": ["necrozma","lunala"], "color": formcolor},
    {"new": "0800_03.png", "id": "ultranecrozma", "roots": ["duskmane","dawnwings"], "color": formcolor},
    {"new": "0984.png", "id": "greattusk", "roots": ["wormhole"], "color": wormholecolor},
    {"new": "0985.png", "id": "screamtail", "roots": ["wormhole"], "color": wormholecolor},
    {"new": "0986.png", "id": "brutebonnet", "roots": ["wormhole"], "color": wormholecolor},
    {"new": "0987.png", "id": "fluttermane", "roots": ["wormhole"], "color": wormholecolor},
    {"new": "0988.png", "id": "slitherwing", "roots": ["wormhole"], "color": wormholecolor},
    {"new": "0989.png", "id": "sandyshocks", "roots": ["wormhole"], "color": wormholecolor},
    {"new": "1005.png", "id": "roaringmoon", "roots": ["wormhole"], "color": wormholecolor},
    {"new": "1009.png", "id": "walkingwake", "roots": ["wormhole"], "color": wormholecolor},
    {"new": "1020.png", "id": "gougingfire", "roots": ["wormhole"], "color": wormholecolor},
    {"new": "1021.png", "id": "ragingbolt", "roots": ["wormhole"], "color": wormholecolor},
    {"new": "1007.png", "id": "koraidon", "roots": ["wormhole"], "color": wormholecolor},
    {"new": "0990.png", "id": "irontreads", "roots": ["wormhole"], "color": wormholecolor},
    {"new": "0991.png", "id": "ironbundle", "roots": ["wormhole"], "color": wormholecolor},
    {"new": "0992.png", "id": "ironhands", "roots": ["wormhole"], "color": wormholecolor},
    {"new": "0993.png", "id": "ironjugulis", "roots": ["wormhole"], "color": wormholecolor},
    {"new": "0994.png", "id": "ironmoth", "roots": ["wormhole"], "color": wormholecolor},
    {"new": "0995.png", "id": "ironthorns", "roots": ["wormhole"], "color": wormholecolor},
    {"new": "1006.png", "id": "ironvaliant", "roots": ["wormhole"], "color": wormholecolor},
    {"new": "1010.png", "id": "ironleaves", "roots": ["wormhole"], "color": wormholecolor},
    {"new": "1022.png", "id": "ironboulder", "roots": ["wormhole"], "color": wormholecolor},
    {"new": "1023.png", "id": "ironcrown", "roots": ["wormhole"], "color": wormholecolor},
    {"new": "1008.png", "id": "miraidon", "roots": ["wormhole"], "color": wormholecolor},
]

addprimordial = [
    {"new": "blackkyurem", "roots": ["kyurem"], "color": formcolor},
    {"new": "whitekyurem", "roots": ["kyurem"], "color": formcolor},
    {"new": "dreamworld", "roots": ["darkrai"], "color": unknowncolor},
] + addabiological + multiverse + addanimals

tree = dogs

additionals = addprimordial