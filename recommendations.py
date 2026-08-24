RECOMMENDATIONS = {

    "crack": {
        "cause": [
            "Improper curing",
            "Drying shrinkage",
            "Thermal movement",
            "Structural loading"
        ],
        "prevention": [
            "Maintain proper curing",
            "Use appropriate water-cement ratio",
            "Provide suitable reinforcement",
            "Control temperature and shrinkage"
        ],
        "action": [
            "Inspect crack width and pattern",
            "Monitor crack progression",
            "Seal suitable non-structural cracks",
            "Obtain structural assessment for significant cracks"
        ]
    },

    "spalling": {
        "cause": [
            "Corrosion of reinforcement",
            "Poor concrete quality",
            "Environmental exposure",
            "Insufficient concrete cover"
        ],
        "prevention": [
            "Provide adequate reinforcement cover",
            "Use durable concrete",
            "Control water penetration",
            "Perform regular inspections"
        ],
        "action": [
            "Remove loose material under professional supervision",
            "Inspect reinforcement condition",
            "Repair damaged concrete using an appropriate repair system",
            "Check for continuing corrosion"
        ]
    },

    "honeycombing": {
        "cause": [
            "Poor compaction",
            "Improper concrete placement",
            "Congested reinforcement",
            "Improper mix workability"
        ],
        "prevention": [
            "Use proper vibration",
            "Ensure suitable concrete workability",
            "Follow correct placing procedures",
            "Maintain proper reinforcement spacing"
        ],
        "action": [
            "Inspect depth and extent",
            "Assess exposed reinforcement if present",
            "Repair using a suitable concrete repair method",
            "Obtain engineering assessment for deep honeycombing"
        ]
    },

    "exposed_rebar": {
        "cause": [
            "Concrete cover deterioration",
            "Corrosion",
            "Poor construction",
            "Concrete spalling"
        ],
        "prevention": [
            "Maintain required concrete cover",
            "Control moisture and chloride exposure",
            "Use durable concrete",
            "Perform periodic maintenance"
        ],
        "action": [
            "Inspect reinforcement condition",
            "Assess corrosion",
            "Protect reinforcement using an appropriate repair system",
            "Restore concrete cover appropriately"
        ]
    }
}


def get_recommendation(defect):

    defect = defect.lower()

    if defect in RECOMMENDATIONS:

        data = RECOMMENDATIONS[defect]

        return {
            "cause": data["cause"],
            "prevention": data["prevention"],
            "action": data["action"]
        }

    return {
        "cause": ["Cause requires further inspection"],
        "prevention": ["Follow standard concrete quality and maintenance practices"],
        "action": ["Consult a qualified professional for detailed assessment"]
    }
