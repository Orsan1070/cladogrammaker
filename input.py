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
splitcolor = "#e4a213"

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

canids = (
    (
        (
            (
                {"color": variantcolor, "tree": (
                    {"color": evocolor, "tree": ["0037.png","0038.png"]},
                    {"color": evocolor, "tree": ["0037_01.png","0038_01.png"]}
                )},
                (
                    (
                        {"color": evocolor, "tree": ["0653.png","0654.png","0655.png"]},
                        {"color": evocolor, "tree": ["0570.png",{"anchor": True, "tree": ({"id": "zoroark", "tree": "0571.png"},{"color": deathcolor, "colorroot": True, "tree": {"color": evocolor, "tree": ["0570_01.png",{"id": "hisuizoroark", "tree": "0571_01.png"}]}})}]},
                    ),
                    {"color": evocolor, "tree": ["0063.png", "0064.png", {"color": megacolor, "tree": ["0065.png","0065_01.png"]}]},
                ),
            ),
            {"color": evocolor, "tree": ["0827.png", "0828.png"]},
        ),
        dogs
    ),
    {"color": evocolor, "tree": ["0133.png", {"anchor": True, "tree": ({"color": gmaxcolor, "colorroot": True, "tree": "gmaxeevee.png"}, "0134.png", "0135.png", "0136.png", "0196.png", "0197.png", "0470.png", "0471.png", "0700.png")}]},
)

bears = (
    (
        {"color": evocolor, "tree": ["0446.png", {"color": megacolor, "tree": ["0143.png","gmaxsnorlax.png"]}]},
        (
            {"color": evocolor, "tree": ["0613.png", "0614.png"]},
            {"color": evocolor, "tree": ["0216.png", "0217.png", {"color": changecolor, "tree": ["0901.png","0901_01.png"]}]},
        )
    ),
    (
        {"color": evocolor, "tree": ["0759.png", "0760.png"]},
        (
            {"color": evocolor, "tree": ["0674.png", "0675.png"]},
            {"color": humanevocolor, "tree": ["0891.png", {"color": gmaxcolor, "tree": ["0892.png",{"anchor": True, "tree": ("gmaxurshifusingle.png","gmaxurshifurapid.png")}]}]},
        )
    )
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
                {"color": evocolor, "tree": ["0906.png","0907.png","0908.png"]},
                (
                    {"color": evocolor, "tree": ["0677.png", {"anchor": True, "tree": ("0678.png", "0678_01.png")}]},
                    (
                        (
                            "0807.png",
                            {"color": evocolor, "tree": ["0403.png","0404.png","0405.png"]},
                        ),
                        (
                            {"color": evocolor, "tree": ["0667.png",{"anchor": True, "tree": ("0668.png", "0668_01.png")}]},
                            {"color": evocolor, "tree": ["0725.png","0726.png","0727.png"]},
                        )
                    ),
                ),
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
        herpestoids,
        cats,
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
            {"color": evocolor, "tree": ["0498.png","0499.png","0500.png"]},
            {"color": evocolor, "tree": ["0915.png",{"anchor": True, "tree": ("0916.png", "0916_01.png")}]},
        ),
    )
)

hipposwhales = (
    (
        {"color": evocolor, "tree": ["0449.png","0450.png"]},
        {"color": evocolor, "tree": ["0293.png","0294.png","0295.png"]},
    ),
    (
        {"color": evocolor, "tree": ["0963.png", {"color": formcolor, "tree": ["0964.png","0964_01.png"]}]},
        (
            {"color": evocolor, "tree": ["0320.png","0321.png"]},
            {"color": evocolor, "tree": ["0974.png","0975.png"]},
        )
    )
)

ruminants = (
    {"color": evocolor, "tree": ["0203.png","0981.png"]},
    (
        (
            (
                (
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
                    "0626.png",
                ),
                "0241.png",
            ),
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
        ),
        (
            (
                {"color": humanevocolor, "tree": ["0234.png","0899.png"]},
                {"color": evocolor, "tree": [{"id": "springdeerling", "tree": "0585.png"},{"id": "springsawsbuck", "tree": "0586.png"}]},
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
    (
        (
            hipposwhales,
            ruminants
        ),
        pigs
    ),
    camels
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
        (
            {"color": evocolor, "tree": ["0111.png","0112.png","0464.png"]},
            {"color": gendercolor, "tree": (
                {"color": evocolor, "tree": ["0029.png","0030.png","0031.png"]},
                {"color": evocolor, "tree": ["0032.png","0033.png","0034.png"]}
            )},
        ),
        {"color": evocolor, "tree": ["0104.png",{"anchor": True, "tree": ("0105.png", "0105_01.png")}]},
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
    eventoed,
    oddtoed
)

bats = (
    (
        {"color": evocolor, "tree": ["0041.png","0042.png","0169.png"]},
        {"color": evocolor, "tree": ["0527.png","0528.png"]},
    ),
    {"color": evocolor, "tree": ["0714.png","0715.png"]},
)

moles = (
    (
        {"color": variantcolor, "tree": (
            {"color": evocolor, "tree": ["0050.png","0051.png"]},
            {"color": evocolor, "tree": ["0050_01.png","0051_01.png"]}
        )},
        {"color": evocolor, "tree": ["0529.png","0530.png"]},
    ),
    {"color": evocolor, "tree": ["0650.png","0651.png","0652.png"]},
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
                    {"color": evocolor, "tree": ["0172.png", "0025.png", {"anchor": True, "tree": ("0026.png","0026_01.png",{"color": gmaxcolor, "tree": "gmaxpikachu.png"},{"color": changecolor, "tree": "0025_08.png"})}]},
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
            {"id": "froslass", "tree": "0478.png"},
            "0802.png",
            "1025.png",
            [{"color": evocolor, "tree": ["0092.png", "0093.png", {"color": megacolor, "tree": ["0094.png",{"anchor": True, "tree": ("0094_01.png",{"color": gmaxcolor, "tree": "gmaxgengar.png"})}]}]}],
            "0442.png",
            [{"color": evocolor, "tree": ["0562.png", {"anchor": True, "tree": ("0563.png",{"color": changecolor, "tree": {"color": evocolor, "tree": ["0562_01.png","0867.png"]}})}]}],
            [{"color": evocolor, "tree": ["0679.png","0680.png","0681.png"]}],
            [{"color": evocolor, "tree": ["1012.png","1013.png"]}],
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
                    {"color": evocolor, "tree": ["0859.png", "0860.png", {"color": gmaxcolor, "tree": ["0861.png","gmaxgrimmsnarl.png"]}]},
                    {"color": evocolor, "tree": ["0856.png", "0857.png", {"color": gmaxcolor, "tree": ["0858.png","gmaxhatterene.png"]}]},
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
                            ungulates,
                            (
                                pangolins,
                                carnivora,
                            )
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
                "0780.png"
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
        {"color": evocolor, "tree": ["0559.png", "0560.png"]},
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
        {"color": evocolor, "tree": "0565.png"},
        (
            {"color": evocolor, "tree": ["0833.png", {"color": gmaxcolor, "tree": ["0834.png","gmaxdrednaw.png"]}]},
            (
                {"color": evocolor, "tree": ["0007.png", "0008.png", {"color": megacolor, "tree": ["0009.png",{"anchor": True, "tree": ("0009_01.png",{"color": gmaxcolor, "tree": "gmaxblastoise.png"})}]}]},
                (
                    (
                        "0776.png",
                        "0324.png"
                    ),
                    {"color": changecolor, "tree": ["mysteryterapagos.png", {"color": formcolor, "tree": ["1024.png","1024_01.png","1024_02.png"]}]},
                )
            )
        )
    )},
],

crocodiles = (
    {"color": evocolor, "tree": ["0909.png", "0910.png", "0911.png"]},
    (
        {"color": evocolor, "tree": ["0158.png", "0159.png", "0160.png"]},
        {"color": evocolor, "tree": ["0551.png", "0552.png", "0553.png"]}
    )
)

flightlessbirds = (
    {"color": evocolor, "tree": ["0084.png", "0085.png"]},
    {"color": evocolor, "tree": ["0955.png", "0956.png"]},
)

ducks = (
    {"color": evocolor, "tree": ["0580.png", "0581.png"]},
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
    )
)

fairybirds = (
    {"color": changecolor, "tree": ["mysteryfezandipiti.png","1016.png"]},
    (
        {"color": evocolor, "tree": ["0175.png","0176.png","0468.png"]},
        {"color": humanevocolor, "tree": ["0682.png","0683.png"]}
    )
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
    {"color": evocolor, "tree": ["0177.png","0178.png"]},
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
        )
    )
)

owls = (
    {"color": evocolor, "tree": ["0722.png", "0723.png", {"anchor": True, "tree": ("0724.png", {"color": humanevocolor, "tree": "0724_01.png"})}]},
    {"color": evocolor, "tree": ["0163.png","0164.png"]}
)

hawks = (
    {"color": evocolor, "tree": ["0629.png","0630.png"]},
    (
        (
            {"color": variantcolor, "tree": ("0145.png","0145_01.png")},
            {"color": evocolor, "tree": ["0627.png", {"anchor": True, "tree": ("0628.png", "0628_01.png")}]},
        ),
        (
            {"color": evocolor, "tree": ["0021.png","0022.png"]},
            "0227.png"
        )
    )
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
                        "0441.png",
                        {"color": variantcolor, "tree": ("0931.png","0931_01.png","0931_02.png","0931_03.png")},
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

#who the hell knows: Aromatisse, Togekiss, Magmortar

birds = (
    {"id": "zolt", "tree": "zolt.png"},
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
                            penguins,
                            divingbirds
                        ),
                        (
                            (
                                (
                                    owls,
                                    hawks
                                ),
                                woodpeckers
                            ),
                            songbirds
                        )
                    )
                )
            )
        ),
        flightlessbirds
    ),
)  

dinosaurs = (
    (
        {"color": gmaxcolor, "tree": ["0131.png","gmaxlapras.png"]},
        {"id": "arcto", "tree": "arcto.png"}
    ),
    (
        {"color": changecolor, "tree": ["0142_01.png", {"color": megacolor, "tree": ["0142.png","0142_01.png"]}]},
        (
            (
                (
                    {"color": evocolor, "tree": ["0410.png", "0411.png"]},
                    {"color": evocolor, "tree": ["0408.png", "0409.png"]}
                ),
                {"id": "draco", "tree": "draco.png"},
            ),
            (
                (
                    (
                        (
                            birds,
                            {"color": evocolor, "tree": ["0566.png", "0567.png"]},
                        ),
                        "0701.png"
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
                                {"color": evocolor, "tree": ["0996.png", "0997.png", "0998.png"]},
                            ),
                        ),
                        {"color": evocolor, "tree": ["0696.png", "0697.png"]},
                    ),
                ),
                (
                    (
                        (
                            {"color": evocolor, "tree": ["0152.png", "0153.png", "0154.png"]},
                            {"color": evocolor, "tree": ["0387.png", "0388.png", "0389.png"]},
                        ),
                        "0357.png",
                    ),
                    {"color": evocolor, "tree": ["0698.png", "0699.png"]},
                ),
            )
        )
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
            crocodiles,
            dinosaurs
        )
    )
)



amphibians = (
    (
        {"color": variantcolor, "tree": (
            {"color": evocolor, "tree": ["0079.png",{"anchor": True, "tree": ("0199.png", ["0080.png",{"color": megacolor, "colorroot": True, "tree": "0080_01.png"}])}]},
            {"color": humanevocolor, "tree": ["0079_01.png",{"anchor": True, "tree": ("0080_02.png","0199_01.png")}]}
        )},
        (
            {"color": variantcolor, "tree": (
                {"color": evocolor, "tree": ["0194.png","0195.png"]},
                {"color": evocolor, "tree": ["0194_01.png","0980.png"]}
            )},
            {"color": evocolor, "tree": ["0258.png", "0259.png", {"color": megacolor, "tree": ["0260.png","0260_01.png"]}]},
        )
    ),
    (
        {"color": evocolor, "tree": ["0001.png", "0002.png", {"color": megacolor, "tree": ["0003.png",{"anchor": True, "tree": ("0003_01.png",{"color": gmaxcolor, "tree": "gmaxvenusaur.png"})}]}]},
        (
            (
                {"color": evocolor, "tree": ["0453.png","0454.png"]},
                {"color": evocolor, "tree": ["0656.png", "0657.png", {"color": megacolor, "tree": ["0658.png","0658_01.png"]}]},
            ),
            (
                {"color": evocolor, "tree": ["0535.png","0536.png","0537.png"]},
                (
                    {"color": evocolor, "tree": ["0938.png","0939.png"]},
                    {"color": evocolor, "tree": ["0060.png", "0061.png", {"anchor": True, "tree": ("0062.png", "0186.png")}]},
                )
            )
        )
    )
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
            {"color": evocolor, "tree": ["0602.png","0603.png","0604.png"]},
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
    {"color": evocolor, "tree": ["0690.png","0691.png"]},
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
                                        (
                                            {"color": evocolor, "tree": ["0456.png","0457.png"]},
                                            (
                                                {"color": evocolor, "tree": ["0170.png","0171.png"]},
                                                tetraodonts
                                            )
                                        ),
                                        {"color": variantcolor, "tree": ("0550.png","0550_01.png",{"color": evocolor, "tree": ["0550_02.png",{"anchor": True, "tree": ("0902.png","0902_01.png")}]})},
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
            {"color": evocolor, "tree": ["0686.png","0687.png"]},
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
            (
                {"color": humanevocolor, "tree": ["0616.png","0617.png"]},
                {"color": evocolor, "tree": ["0090.png","0091.png"]},
            ),
            {"color": variantcolor, "tree": (
                {"color": evocolor, "tree": ["0422.png","0423.png"]},
                {"color": evocolor, "tree": ["0422_01.png","0423_01.png"]},
            )},
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
    {"color": evocolor, "tree": ["0543.png","0544.png","0545.png"]},
)

crustaceans = (
    {"color": evocolor, "tree": ["0688.png","0689.png"]},
    (
        (
            (
                ["0347.png", 
                    {"anchor": True, "tree":(
                        {"color": evocolor, "tree": "0348.png"},
                        (
                            {"color": evocolor, "tree": ["0046.png","0047.png"]},
                            {"color": evocolor, "tree": ["0557.png","0558.png"]},
                        )
                    )}
                ]
            ),
            (
                {"color": evocolor, "tree": ["0692.png","0693.png"]},
                (
                    (
                        {"color": evocolor, "tree": ["0098.png",{"color": gmaxcolor, "tree": ["0099.png","gmaxkingler.png"]}]},
                        (
                            "0950.png",
                            {"color": evocolor, "tree": ["0739.png","0740.png"]},
                        )
                    ),
                    {"color": evocolor, "tree": ["0341.png","0342.png"]},
                )
            )
        ),
        {"color": evocolor, "tree": ["0767.png","0768.png"]},
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
        {"color": evocolor, "tree": ["0540.png","0541.png","0542.png"]}
    ),
    (
        {"color": evocolor, "tree": ["0013.png","0014.png",{"color": megacolor, "tree": ["0015.png","0015_01.png"]}]},
        {"color": evocolor, "tree": ["0415.png","0416.png"]}
    )
)

beetles = (
    (
        (
            (
                {"color": megacolor, "tree": ["0214.png","0214_01.png"]},
                (
                    (
                        {"color": evocolor, "tree": ["0624.png","0625.png","0983.png"]},
                        "0870.png"
                    ),
                    {"color": humanevocolor, "tree": ["0588.png","0589.png"]},
                )
            ),
            (
                {"color": megacolor, "tree": ["0127.png","0127_01.png"]},
                {"color": evocolor, "tree": ["0736.png","0737.png","0738.png"]}
            )
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

    )
)

insects = (
    dragonflies,
    (
        (
            truebugs,
            (
                beesants,
                (
                    beetles,
                    moths
                ),
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
        molluscs,
        worms
    ),
    arthropods
)

addmammals = [
    {"new": "hisuizoroark", "roots": ["zoroark"], "color": deathcolor},
    {"new": "0971.png", "dontaffectvert": True, "id": "greavard", "roots": ["maschiff"], "color": "#ffffff"},
    {"new": "0972.png", "id": "houndstone", "roots": ["greavard"], "color": evocolor},
    {"new": "gholdengo", "roots": ["roaminggimmighoul"], "color": evocolor},
    {"new": "0361.png", "id": "snorunt", "roots": [], "color": evocolor},
    {"new": "glalie", "roots": ["snorunt"], "color": evocolor},
    {"new": "froslass", "roots": ["snorunt"], "color": evocolor},
    {"new": "0343.png", "id": "baltoy", "roots": [], "color": evocolor},
    {"new": "claydol", "roots": ["baltoy"], "color": evocolor},
]

addbirds = [
    {"new": "sensu", "roots": ["pompom","pau"], "color": formcolor, "dontaffectvert": True,},
    {"new": "pau", "roots": ["pompom"], "color": formcolor, "dontaffectvert": True,},
]

addreptiles = [
    {"new": "gmaxtoxtricity.png", "roots": ["ampedtox", "lowkeytox"], "color": gmaxcolor},
    {"new": "gmaxapple.png", "roots": ["flapple", "appletun"], "color": gmaxcolor},
    {"new": "0880.png", "id": "dracozolt", "roots": ["draco"], "color": changecolor},
    {"new": "0881.png", "id": "arctozolt", "roots": ["arcto"], "color": changecolor},
    {"new": "zolt", "roots": ["dracozolt","arctozolt"], "color": changecolor},
] + addbirds

addfish = [
    #{"new": "0882.png", "id": "dracovish", "roots": ["vish"], "color": changecolor},
    #{"new": "0883.png", "id": "arctovish", "roots": ["vish"], "color": changecolor},
    #{"new": "draco", "roots": ["dracovish"], "color": changecolor},
    #{"new": "arcto", "roots": ["arctovish"], "color": changecolor},
] + addmammals + addreptiles

tree = mammals

additionals = addmammals