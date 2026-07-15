# EVENTS DATABASE

events = [
    
    # CATEGORY 1: ENVIRONMENT AND NATURAL DISASTERS
    {
        "event_description": "A major storm damages parts of the city, disrupting daily life and putting pressure on emergency services.",
        "choices": [
            {
                "choice_description": "Launch a large emergency response and immediately repair damaged areas.",
                "population_change": 2,
                "budget_change": -12,
                "approval_change": 8,
                "infrastructure_change": 10
            },
            {
                "choice_description": "Repair the most important areas first while delaying less urgent repairs.",
                "population_change": 0,
                "budget_change": -5,
                "approval_change": 3,
                "infrastructure_change": 5
            },
            {
                "choice_description": "Avoid major spending and wait for conditions to improve naturally.",
                "population_change": -2,
                "budget_change": 2,
                "approval_change": -8,
                "infrastructure_change": -6
            }
        ]
    },
    {
        "event_description": "Heavy rainfall overwhelms the city's drainage systems, causing flooding in several neighborhoods.",
        "choices": [
            {
                "choice_description": "Invest heavily in flood prevention systems and repair damaged areas.",
                "population_change": 2,
                "budget_change": -14,
                "approval_change": 9,
                "infrastructure_change": 12
            },
            {
                "choice_description": "Repair the worst affected areas and improve drainage gradually.",
                "population_change": 0,
                "budget_change": -6,
                "approval_change": 4,
                "infrastructure_change": 6
            },
            {
                "choice_description": "Limit spending and focus only on emergency cleanup.",
                "population_change": -2,
                "budget_change": 1,
                "approval_change": -7,
                "infrastructure_change": -5
            }
        ]
    },
    {
        "event_description": "A wildfire near the city threatens communities and forces officials to prepare emergency plans.",
        "choices": [
            {
                "choice_description": "Fund a major wildfire prevention and response program.",
                "population_change": 2,
                "budget_change": -10,
                "approval_change": 8,
                "infrastructure_change": 7
            },
            {
                "choice_description": "Improve emergency services while keeping costs under control.",
                "population_change": 0,
                "budget_change": -5,
                "approval_change": 4,
                "infrastructure_change": 4
            },
            {
                "choice_description": "Avoid major spending unless the wildfire becomes a direct threat.",
                "population_change": -3,
                "budget_change": 3,
                "approval_change": -8,
                "infrastructure_change": -4
            }
        ]
    },
    {
        "event_description": "A powerful earthquake damages buildings, roads, and important city infrastructure.",
        "choices": [
            {
                "choice_description": "Begin a massive rebuilding effort and upgrade damaged infrastructure.",
                "population_change": 3,
                "budget_change": -15,
                "approval_change": 10,
                "infrastructure_change": 15
            },
            {
                "choice_description": "Focus on repairing essential services before rebuilding everything.",
                "population_change": 0,
                "budget_change": -7,
                "approval_change": 5,
                "infrastructure_change": 7
            },
            {
                "choice_description": "Delay reconstruction to protect the city's finances.",
                "population_change": -4,
                "budget_change": 4,
                "approval_change": -10,
                "infrastructure_change": -10
            }
        ]
    },
    {
        "event_description": "A prolonged drought reduces the city's water supply and creates concerns about future shortages.",
        "choices": [
            {
                "choice_description": "Build new water infrastructure and launch conservation programs.",
                "population_change": 2,
                "budget_change": -12,
                "approval_change": 8,
                "infrastructure_change": 10
            },
            {
                "choice_description": "Introduce moderate restrictions while studying long-term solutions.",
                "population_change": 0,
                "budget_change": -3,
                "approval_change": 2,
                "infrastructure_change": 3
            },
            {
                "choice_description": "Avoid restrictions and hope conditions improve naturally.",
                "population_change": -3,
                "budget_change": 2,
                "approval_change": -9,
                "infrastructure_change": -5
            }
        ]
    },
    {
        "event_description": "A record-breaking heat wave strains the city's power grid and puts vulnerable residents at risk.",
        "choices": [
            {
                "choice_description": "Open emergency cooling centers and invest in upgrades to the power grid.",
                "population_change": 2,
                "budget_change": -10,
                "approval_change": 9,
                "infrastructure_change": 8
            },
            {
                "choice_description": "Open temporary cooling centers and ask residents to conserve electricity.",
                "population_change": 0,
                "budget_change": -4,
                "approval_change": 4,
                "infrastructure_change": 2
            },
            {
                "choice_description": "Issue a heat advisory and avoid additional city spending.",
                "population_change": -2,
                "budget_change": 2,
                "approval_change": -8,
                "infrastructure_change": -4
            }
        ]
    },
    {
        "event_description": "Tests reveal dangerous pollution levels in a river that supplies water to parts of the city.",
        "choices": [
            {
                "choice_description": "Shut down the affected facilities and fund an immediate cleanup operation.",
                "population_change": 1,
                "budget_change": -12,
                "approval_change": 9,
                "infrastructure_change": 7
            },
            {
                "choice_description": "Fine the responsible companies and require them to fund cleanup efforts.",
                "population_change": 0,
                "budget_change": 4,
                "approval_change": 5,
                "infrastructure_change": 3
            },
            {
                "choice_description": "Delay action until officials complete a longer investigation.",
                "population_change": -3,
                "budget_change": 1,
                "approval_change": -10,
                "infrastructure_change": -5
            }
        ]
    },
    {
        "event_description": "Energy companies propose a large renewable energy project that could reduce the city's reliance on fossil fuels.",
        "choices": [
            {
                "choice_description": "Provide major city funding to accelerate construction of the project.",
                "population_change": 3,
                "budget_change": -13,
                "approval_change": 8,
                "infrastructure_change": 10
            },
            {
                "choice_description": "Approve the project but require private companies to cover most of the cost.",
                "population_change": 2,
                "budget_change": 1,
                "approval_change": 4,
                "infrastructure_change": 6
            },
            {
                "choice_description": "Reject the project and continue using the city's existing energy system.",
                "population_change": -1,
                "budget_change": 3,
                "approval_change": -5,
                "infrastructure_change": -2
            }
        ]
    },
    {
        "event_description": "City officials propose stricter environmental regulations, but local businesses warn that the new rules could increase costs.",
        "choices": [
            {
                "choice_description": "Adopt the regulations immediately and enforce strict environmental standards.",
                "population_change": 1,
                "budget_change": -5,
                "approval_change": 6,
                "infrastructure_change": 5
            },
            {
                "choice_description": "Introduce the regulations gradually and provide businesses time to adapt.",
                "population_change": 1,
                "budget_change": -2,
                "approval_change": 3,
                "infrastructure_change": 3
            },
            {
                "choice_description": "Reject the regulations to protect local businesses from additional costs.",
                "population_change": 0,
                "budget_change": 4,
                "approval_change": -6,
                "infrastructure_change": -3
            }
        ]
    },
    {
        "event_description": "A proposed development project would create new housing and businesses but destroy part of a protected natural area.",
        "choices": [
            {
                "choice_description": "Cancel the development and permanently protect the natural area.",
                "population_change": -2,
                "budget_change": -3,
                "approval_change": 6,
                "infrastructure_change": 2
            },
            {
                "choice_description": "Approve a smaller development while preserving most of the protected land.",
                "population_change": 3,
                "budget_change": 3,
                "approval_change": 4,
                "infrastructure_change": 4
            },
            {
                "choice_description": "Approve the full development project to encourage rapid city growth.",
                "population_change": 6,
                "budget_change": 8,
                "approval_change": -7,
                "infrastructure_change": -5
            }
        ]
    },

    # CATEGORY 2: ECONOMY AND BUSINESS
    {
        "event_description": "A major technology company is considering moving its headquarters to the city, promising thousands of new jobs.",
        "choices": [
            {
                "choice_description": "Offer major tax incentives and approve the company's plans immediately.",
                "population_change": 6,
                "budget_change": -12,
                "approval_change": 6,
                "infrastructure_change": -6
            },
            {
                "choice_description": "Negotiate a smaller incentive package and require investment in city infrastructure.",
                "population_change": 4,
                "budget_change": 1,
                "approval_change": 4,
                "infrastructure_change": 5
            },
            {
                "choice_description": "Reject the proposal to avoid placing additional pressure on city services.",
                "population_change": -1,
                "budget_change": 2,
                "approval_change": -5,
                "infrastructure_change": 2
            }
        ]
    },
    {
        "event_description": "A manufacturing company proposes building a large factory on the outskirts of the city, creating jobs but raising pollution concerns.",
        "choices": [
            {
                "choice_description": "Approve the factory without additional restrictions to encourage economic growth.",
                "population_change": 5,
                "budget_change": 8,
                "approval_change": -5,
                "infrastructure_change": -6
            },
            {
                "choice_description": "Approve the factory with strict environmental and infrastructure requirements.",
                "population_change": 3,
                "budget_change": 3,
                "approval_change": 5,
                "infrastructure_change": 3
            },
            {
                "choice_description": "Reject the factory to prevent pollution and industrial expansion.",
                "population_change": -2,
                "budget_change": -3,
                "approval_change": 3,
                "infrastructure_change": 1
            }
        ]
    },
    {
        "event_description": "One of the city's largest employers announces plans to close its local operations, putting thousands of jobs at risk.",
        "choices": [
            {
                "choice_description": "Provide financial assistance to convince the company to remain in the city.",
                "population_change": 2,
                "budget_change": -13,
                "approval_change": 7,
                "infrastructure_change": 0
            },
            {
                "choice_description": "Fund job training programs to help affected workers find new employment.",
                "population_change": 0,
                "budget_change": -6,
                "approval_change": 5,
                "infrastructure_change": 2
            },
            {
                "choice_description": "Allow the company to leave and let the economy adjust naturally.",
                "population_change": -6,
                "budget_change": 3,
                "approval_change": -9,
                "infrastructure_change": 0
            }
        ]
    },
    {
        "event_description": "A wave of new startups has transformed the city into a growing technology hub, attracting workers and investors.",
        "choices": [
            {
                "choice_description": "Create a major city investment fund to support promising startups.",
                "population_change": 6,
                "budget_change": -11,
                "approval_change": 7,
                "infrastructure_change": -4
            },
            {
                "choice_description": "Offer limited incentives while allowing private investors to lead the industry's growth.",
                "population_change": 4,
                "budget_change": 2,
                "approval_change": 4,
                "infrastructure_change": -2
            },
            {
                "choice_description": "Avoid government involvement and focus resources on established industries.",
                "population_change": -2,
                "budget_change": 3,
                "approval_change": -5,
                "infrastructure_change": 1
            }
        ]
    },
    {
        "event_description": "An economic recession causes businesses across the city to close and unemployment to rise.",
        "choices": [
            {
                "choice_description": "Launch a major economic relief program for businesses and unemployed residents.",
                "population_change": 2,
                "budget_change": -15,
                "approval_change": 10,
                "infrastructure_change": 1
            },
            {
                "choice_description": "Provide targeted assistance to the industries and residents most affected by the recession.",
                "population_change": 0,
                "budget_change": -7,
                "approval_change": 5,
                "infrastructure_change": 0
            },
            {
                "choice_description": "Reduce city spending and wait for the economy to recover naturally.",
                "population_change": -5,
                "budget_change": 6,
                "approval_change": -10,
                "infrastructure_change": -2
            }
        ]
    },
    {
        "event_description": "The city suddenly becomes a popular tourist destination, bringing large crowds and new economic opportunities.",
        "choices": [
            {
                "choice_description": "Invest heavily in tourism infrastructure and launch a major advertising campaign.",
                "population_change": 4,
                "budget_change": -10,
                "approval_change": 7,
                "infrastructure_change": 6
            },
            {
                "choice_description": "Support tourism with limited investments while allowing local businesses to handle growth.",
                "population_change": 2,
                "budget_change": 3,
                "approval_change": 4,
                "infrastructure_change": 1
            },
            {
                "choice_description": "Avoid encouraging additional tourism to prevent overcrowding.",
                "population_change": -1,
                "budget_change": -2,
                "approval_change": -4,
                "infrastructure_change": 3
            }
        ]
    },
    {
        "event_description": "City leaders propose changing local tax rates as officials debate how to increase government revenue.",
        "choices": [
            {
                "choice_description": "Raise taxes significantly to increase funding for city services.",
                "population_change": -3,
                "budget_change": 12,
                "approval_change": -9,
                "infrastructure_change": 5
            },
            {
                "choice_description": "Introduce a small tax increase and direct the additional revenue toward essential services.",
                "population_change": -1,
                "budget_change": 6,
                "approval_change": -2,
                "infrastructure_change": 3
            },
            {
                "choice_description": "Cut taxes to encourage economic growth and attract new residents.",
                "population_change": 4,
                "budget_change": -8,
                "approval_change": 7,
                "infrastructure_change": -3
            }
        ]
    },
    {
        "event_description": "Small businesses across the city report rising costs and ask the government for financial support.",
        "choices": [
            {
                "choice_description": "Create a large grant program to support struggling local businesses.",
                "population_change": 2,
                "budget_change": -11,
                "approval_change": 8,
                "infrastructure_change": 1
            },
            {
                "choice_description": "Offer temporary tax relief to qualifying small businesses.",
                "population_change": 1,
                "budget_change": -5,
                "approval_change": 5,
                "infrastructure_change": 0
            },
            {
                "choice_description": "Decline financial assistance and allow businesses to adapt independently.",
                "population_change": -3,
                "budget_change": 4,
                "approval_change": -8,
                "infrastructure_change": 0
            }
        ]
    },
    {
        "event_description": "A professional sports team offers to relocate to the city if officials help fund a new stadium.",
        "choices": [
            {
                "choice_description": "Use city funds to build a large modern stadium and attract the team.",
                "population_change": 5,
                "budget_change": -15,
                "approval_change": 8,
                "infrastructure_change": 7
            },
            {
                "choice_description": "Offer limited funding and require the team's owners to pay most construction costs.",
                "population_change": 3,
                "budget_change": -4,
                "approval_change": 5,
                "infrastructure_change": 4
            },
            {
                "choice_description": "Reject public funding for the stadium and allow the team to relocate elsewhere.",
                "population_change": -1,
                "budget_change": 4,
                "approval_change": -5,
                "infrastructure_change": 1
            }
        ]
    },
    {
        "event_description": "International investors offer to finance several major projects in the city but request favorable development agreements in return.",
        "choices": [
            {
                "choice_description": "Accept the investment and approve the requested development agreements.",
                "population_change": 6,
                "budget_change": 10,
                "approval_change": -5,
                "infrastructure_change": 8
            },
            {
                "choice_description": "Negotiate stricter agreements while accepting a smaller amount of investment.",
                "population_change": 3,
                "budget_change": 5,
                "approval_change": 4,
                "infrastructure_change": 5
            },
            {
                "choice_description": "Reject the investment to maintain greater control over city development.",
                "population_change": -1,
                "budget_change": -3,
                "approval_change": 3,
                "infrastructure_change": 0
            }
        ]
    },

    # CATEGORY 3: URBAN DEVELOPMENT AND INFRASTRUCTURE
    {
        "event_description": "Rapid population growth has caused housing prices to rise sharply, leaving many residents struggling to find affordable homes.",
        "choices": [
            {
                "choice_description": "Build large amounts of publicly funded housing across the city.",
                "population_change": 4,
                "budget_change": -14,
                "approval_change": 9,
                "infrastructure_change": 6
            },
            {
                "choice_description": "Offer incentives for private developers to build more housing.",
                "population_change": 5,
                "budget_change": -5,
                "approval_change": 4,
                "infrastructure_change": 2
            },
            {
                "choice_description": "Avoid intervention and allow the housing market to adjust naturally.",
                "population_change": -4,
                "budget_change": 3,
                "approval_change": -9,
                "infrastructure_change": 0
            }
        ]
    },
    {
        "event_description": "Increasing traffic congestion has led residents to demand major improvements to the city's public transportation system.",
        "choices": [
            {
                "choice_description": "Build a major new public transit network across the city.",
                "population_change": 5,
                "budget_change": -15,
                "approval_change": 9,
                "infrastructure_change": 14
            },
            {
                "choice_description": "Expand existing transit routes and increase service frequency.",
                "population_change": 2,
                "budget_change": -7,
                "approval_change": 5,
                "infrastructure_change": 7
            },
            {
                "choice_description": "Maintain the existing system and focus spending on other city priorities.",
                "population_change": -2,
                "budget_change": 3,
                "approval_change": -7,
                "infrastructure_change": -4
            }
        ]
    },
    {
        "event_description": "Engineers warn that one of the city's busiest bridges is aging and will require major repairs in the near future.",
        "choices": [
            {
                "choice_description": "Replace the bridge entirely with a larger and more modern structure.",
                "population_change": 2,
                "budget_change": -15,
                "approval_change": 7,
                "infrastructure_change": 15
            },
            {
                "choice_description": "Fund essential repairs to extend the bridge's lifespan.",
                "population_change": 0,
                "budget_change": -7,
                "approval_change": 3,
                "infrastructure_change": 7
            },
            {
                "choice_description": "Delay repairs until the bridge shows more serious signs of deterioration.",
                "population_change": -2,
                "budget_change": 4,
                "approval_change": -7,
                "infrastructure_change": -8
            }
        ]
    },
    {
        "event_description": "New neighborhoods on the edge of the city are growing rapidly, but the existing road network cannot handle the increased traffic.",
        "choices": [
            {
                "choice_description": "Construct a major network of new roads and highways.",
                "population_change": 5,
                "budget_change": -13,
                "approval_change": 6,
                "infrastructure_change": 13
            },
            {
                "choice_description": "Expand the busiest roads and improve major intersections.",
                "population_change": 2,
                "budget_change": -6,
                "approval_change": 4,
                "infrastructure_change": 7
            },
            {
                "choice_description": "Delay road expansion and encourage residents to use existing transportation options.",
                "population_change": -3,
                "budget_change": 3,
                "approval_change": -7,
                "infrastructure_change": -5
            }
        ]
    },
    {
        "event_description": "The city's airport is approaching maximum capacity, and officials propose a major expansion to support future growth.",
        "choices": [
            {
                "choice_description": "Approve a large airport expansion with new terminals and runways.",
                "population_change": 6,
                "budget_change": -15,
                "approval_change": 5,
                "infrastructure_change": 14
            },
            {
                "choice_description": "Expand the airport gradually to manage costs and limit disruption.",
                "population_change": 3,
                "budget_change": -7,
                "approval_change": 4,
                "infrastructure_change": 7
            },
            {
                "choice_description": "Reject the expansion and maintain the airport at its current size.",
                "population_change": -2,
                "budget_change": 4,
                "approval_change": -5,
                "infrastructure_change": -3
            }
        ]
    },
    {
        "event_description": "The city's aging power grid is struggling to meet rising electricity demand, causing increasingly frequent outages.",
        "choices": [
            {
                "choice_description": "Completely modernize the power grid with new technology and expanded capacity.",
                "population_change": 3,
                "budget_change": -15,
                "approval_change": 8,
                "infrastructure_change": 15
            },
            {
                "choice_description": "Upgrade the most unreliable parts of the power grid first.",
                "population_change": 1,
                "budget_change": -7,
                "approval_change": 4,
                "infrastructure_change": 8
            },
            {
                "choice_description": "Delay major upgrades and encourage residents to reduce electricity use.",
                "population_change": -3,
                "budget_change": 3,
                "approval_change": -8,
                "infrastructure_change": -7
            }
        ]
    },
    {
        "event_description": "Aging water pipes are causing leaks and service disruptions throughout several parts of the city.",
        "choices": [
            {
                "choice_description": "Replace the city's aging water system with modern infrastructure.",
                "population_change": 3,
                "budget_change": -14,
                "approval_change": 8,
                "infrastructure_change": 14
            },
            {
                "choice_description": "Replace the most damaged pipes and repair leaks as they appear.",
                "population_change": 1,
                "budget_change": -6,
                "approval_change": 4,
                "infrastructure_change": 7
            },
            {
                "choice_description": "Postpone major repairs and continue using temporary fixes.",
                "population_change": -3,
                "budget_change": 4,
                "approval_change": -8,
                "infrastructure_change": -7
            }
        ]
    },
    {
        "event_description": "The city's downtown district has declined as businesses close and residents move to newer neighborhoods.",
        "choices": [
            {
                "choice_description": "Launch a major downtown redevelopment project with new housing, businesses, and public spaces.",
                "population_change": 5,
                "budget_change": -13,
                "approval_change": 8,
                "infrastructure_change": 11
            },
            {
                "choice_description": "Offer incentives for private businesses and developers to invest in downtown.",
                "population_change": 3,
                "budget_change": -4,
                "approval_change": 4,
                "infrastructure_change": 5
            },
            {
                "choice_description": "Allow development to shift toward newer parts of the city.",
                "population_change": -2,
                "budget_change": 3,
                "approval_change": -6,
                "infrastructure_change": -4
            }
        ]
    },
    {
        "event_description": "Residents are demanding more parks, sports facilities, and public spaces as the city becomes increasingly crowded.",
        "choices": [
            {
                "choice_description": "Build a large network of new parks and recreation facilities.",
                "population_change": 4,
                "budget_change": -11,
                "approval_change": 10,
                "infrastructure_change": 7
            },
            {
                "choice_description": "Renovate existing parks and create several smaller public spaces.",
                "population_change": 2,
                "budget_change": -5,
                "approval_change": 6,
                "infrastructure_change": 4
            },
            {
                "choice_description": "Prioritize essential infrastructure instead of recreational projects.",
                "population_change": -1,
                "budget_change": 3,
                "approval_change": -7,
                "infrastructure_change": 2
            }
        ]
    },
    {
        "event_description": "Technology companies propose installing sensors and automated systems throughout the city to improve traffic, utilities, and public services.",
        "choices": [
            {
                "choice_description": "Launch a citywide smart technology program and modernize public systems.",
                "population_change": 4,
                "budget_change": -13,
                "approval_change": 7,
                "infrastructure_change": 13
            },
            {
                "choice_description": "Test the technology in several neighborhoods before expanding the program.",
                "population_change": 2,
                "budget_change": -5,
                "approval_change": 4,
                "infrastructure_change": 6
            },
            {
                "choice_description": "Reject the proposal due to cost and privacy concerns.",
                "population_change": -1,
                "budget_change": 4,
                "approval_change": 2,
                "infrastructure_change": -3
            }
        ]
    },

    # CATEGORY 4: SOCIETY AND PUBLIC SERVICES
    {
        "event_description": "Hospitals and clinics across the city are struggling to meet rising demand, leaving many residents without reliable access to healthcare.",
        "choices": [
            {
                "choice_description": "Build new public health facilities and significantly expand healthcare services.",
                "population_change": 5,
                "budget_change": -15,
                "approval_change": 10,
                "infrastructure_change": 7
            },
            {
                "choice_description": "Provide funding to expand existing hospitals and community clinics.",
                "population_change": 2,
                "budget_change": -7,
                "approval_change": 6,
                "infrastructure_change": 3
            },
            {
                "choice_description": "Allow private healthcare providers to respond to the increased demand.",
                "population_change": -3,
                "budget_change": 3,
                "approval_change": -8,
                "infrastructure_change": 0
            }
        ]
    },
    {
        "event_description": "Schools across the city report overcrowded classrooms, aging facilities, and shortages of teachers and educational resources.",
        "choices": [
            {
                "choice_description": "Launch a major education investment program to build schools and hire additional teachers.",
                "population_change": 5,
                "budget_change": -14,
                "approval_change": 10,
                "infrastructure_change": 8
            },
            {
                "choice_description": "Increase school funding to address the most urgent problems.",
                "population_change": 2,
                "budget_change": -6,
                "approval_change": 5,
                "infrastructure_change": 3
            },
            {
                "choice_description": "Maintain current education funding and ask schools to manage their existing resources.",
                "population_change": -3,
                "budget_change": 4,
                "approval_change": -9,
                "infrastructure_change": -2
            }
        ]
    },
    {
        "event_description": "Crime rates have risen across several neighborhoods, increasing public concern about safety.",
        "choices": [
            {
                "choice_description": "Significantly expand police staffing and invest in new public safety programs.",
                "population_change": 2,
                "budget_change": -12,
                "approval_change": 8,
                "infrastructure_change": 3
            },
            {
                "choice_description": "Increase targeted patrols and fund community-based crime prevention programs.",
                "population_change": 1,
                "budget_change": -6,
                "approval_change": 5,
                "infrastructure_change": 1
            },
            {
                "choice_description": "Avoid major policy changes and allow existing departments to handle the increase.",
                "population_change": -4,
                "budget_change": 3,
                "approval_change": -10,
                "infrastructure_change": -2
            }
        ]
    },
    {
        "event_description": "Public demonstrations call for major changes to the city's policing policies and greater oversight of law enforcement.",
        "choices": [
            {
                "choice_description": "Implement major policing reforms and create a new independent oversight system.",
                "population_change": 2,
                "budget_change": -8,
                "approval_change": 7,
                "infrastructure_change": 1
            },
            {
                "choice_description": "Introduce limited reforms while increasing training and internal accountability.",
                "population_change": 1,
                "budget_change": -4,
                "approval_change": 4,
                "infrastructure_change": 1
            },
            {
                "choice_description": "Reject major reforms and publicly defend the city's existing policing policies.",
                "population_change": -2,
                "budget_change": 2,
                "approval_change": -8,
                "infrastructure_change": 0
            }
        ]
    },
    {
        "event_description": "The number of residents experiencing homelessness has increased significantly, placing pressure on shelters and public services.",
        "choices": [
            {
                "choice_description": "Launch a major housing and support program for residents experiencing homelessness.",
                "population_change": 3,
                "budget_change": -14,
                "approval_change": 8,
                "infrastructure_change": 5
            },
            {
                "choice_description": "Expand temporary shelters and increase funding for existing support services.",
                "population_change": 1,
                "budget_change": -7,
                "approval_change": 5,
                "infrastructure_change": 2
            },
            {
                "choice_description": "Increase enforcement of public camping restrictions instead of expanding city programs.",
                "population_change": -3,
                "budget_change": 1,
                "approval_change": -7,
                "infrastructure_change": 1
            }
        ]
    },
    {
        "event_description": "Rapid population growth has placed increasing pressure on city services, schools, hospitals, and emergency departments.",
        "choices": [
            {
                "choice_description": "Launch a major expansion of public services to prepare for continued population growth.",
                "population_change": 5,
                "budget_change": -14,
                "approval_change": 9,
                "infrastructure_change": 8
            },
            {
                "choice_description": "Expand the most heavily used city services and monitor future demand.",
                "population_change": 2,
                "budget_change": -6,
                "approval_change": 5,
                "infrastructure_change": 4
            },
            {
                "choice_description": "Limit new spending and require existing departments to manage the increased demand.",
                "population_change": -3,
                "budget_change": 4,
                "approval_change": -9,
                "infrastructure_change": -4
            }
        ]
    },
    {
        "event_description": "Community organizations request additional city funding for youth programs, senior services, and neighborhood centers.",
        "choices": [
            {
                "choice_description": "Create a major citywide community services initiative.",
                "population_change": 3,
                "budget_change": -11,
                "approval_change": 10,
                "infrastructure_change": 4
            },
            {
                "choice_description": "Provide additional funding to the most heavily used community programs.",
                "population_change": 1,
                "budget_change": -5,
                "approval_change": 6,
                "infrastructure_change": 2
            },
            {
                "choice_description": "Maintain current funding and encourage organizations to seek private donations.",
                "population_change": -1,
                "budget_change": 3,
                "approval_change": -7,
                "infrastructure_change": 0
            }
        ]
    },
    {
        "event_description": "Thousands of residents gather downtown for a large protest demanding changes to several city policies.",
        "choices": [
            {
                "choice_description": "Meet with protest organizers and publicly commit to reviewing the city's policies.",
                "population_change": 1,
                "budget_change": -3,
                "approval_change": 8,
                "infrastructure_change": 0
            },
            {
                "choice_description": "Allow the protest to continue while increasing security around government buildings.",
                "population_change": 0,
                "budget_change": -5,
                "approval_change": 2,
                "infrastructure_change": 1
            },
            {
                "choice_description": "Order officials to disperse the protest and restore normal city operations.",
                "population_change": -2,
                "budget_change": 1,
                "approval_change": -10,
                "infrastructure_change": -2
            }
        ]
    },
    {
        "event_description": "Local cultural organizations propose hosting a major citywide festival expected to attract residents and visitors.",
        "choices": [
            {
                "choice_description": "Fully fund the festival and expand it into a major annual city event.",
                "population_change": 3,
                "budget_change": -10,
                "approval_change": 10,
                "infrastructure_change": 3
            },
            {
                "choice_description": "Provide limited city funding and require organizers to secure private sponsors.",
                "population_change": 2,
                "budget_change": -3,
                "approval_change": 6,
                "infrastructure_change": 1
            },
            {
                "choice_description": "Decline city funding and allow organizers to hold a smaller privately funded event.",
                "population_change": 0,
                "budget_change": 2,
                "approval_change": -5,
                "infrastructure_change": 0
            }
        ]
    },
    {
        "event_description": "A rapidly spreading illness has caused a public health emergency, overwhelming hospitals and disrupting daily life across the city.",
        "choices": [
            {
                "choice_description": "Launch a major emergency health response and provide extensive support to affected residents.",
                "population_change": 2,
                "budget_change": -15,
                "approval_change": 10,
                "infrastructure_change": 4
            },
            {
                "choice_description": "Expand hospital capacity and introduce targeted public health measures.",
                "population_change": 0,
                "budget_change": -8,
                "approval_change": 5,
                "infrastructure_change": 2
            },
            {
                "choice_description": "Avoid major restrictions and focus on keeping businesses and city services operating.",
                "population_change": -6,
                "budget_change": 5,
                "approval_change": -10,
                "infrastructure_change": -2
            }
        ]
    },

    # CATEGORY 5: GOVERNMENT AND POLITICS
    {
        "event_description": "Election season has begun, and your opponents are criticizing your administration's record across the city.",
        "choices": [
            {
                "choice_description": "Launch a major campaign highlighting your administration's accomplishments.",
                "population_change": 0,
                "budget_change": -8,
                "approval_change": 10,
                "infrastructure_change": 0
            },
            {
                "choice_description": "Continue governing normally and allow your record to speak for itself.",
                "population_change": 0,
                "budget_change": 1,
                "approval_change": 2,
                "infrastructure_change": 1
            },
            {
                "choice_description": "Attack your opponents and blame them for the city's remaining problems.",
                "population_change": -1,
                "budget_change": 2,
                "approval_change": -7,
                "infrastructure_change": 0
            }
        ]
    },
    {
        "event_description": "A corruption scandal involving several senior city officials has damaged public trust in your administration.",
        "choices": [
            {
                "choice_description": "Launch a full independent investigation and remove officials implicated in the scandal.",
                "population_change": 0,
                "budget_change": -7,
                "approval_change": 9,
                "infrastructure_change": 0
            },
            {
                "choice_description": "Conduct an internal review and introduce new ethics rules for city officials.",
                "population_change": 0,
                "budget_change": -3,
                "approval_change": 4,
                "infrastructure_change": 0
            },
            {
                "choice_description": "Dismiss the scandal as exaggerated and defend your administration.",
                "population_change": -2,
                "budget_change": 1,
                "approval_change": -12,
                "infrastructure_change": 0
            }
        ]
    },
    {
        "event_description": "The city council rejects one of your major policy proposals, creating a public political dispute at City Hall.",
        "choices": [
            {
                "choice_description": "Negotiate with council members and revise the proposal to gain their support.",
                "population_change": 0,
                "budget_change": -2,
                "approval_change": 5,
                "infrastructure_change": 2
            },
            {
                "choice_description": "Abandon the proposal and focus on policies with broader political support.",
                "population_change": 0,
                "budget_change": 2,
                "approval_change": 1,
                "infrastructure_change": -1
            },
            {
                "choice_description": "Publicly criticize the city council and pressure members to approve the original proposal.",
                "population_change": -1,
                "budget_change": 0,
                "approval_change": -7,
                "infrastructure_change": -2
            }
        ]
    },
    {
        "event_description": "A neighboring city proposes a major regional partnership to coordinate transportation, economic development, and public services.",
        "choices": [
            {
                "choice_description": "Fully join the partnership and commit significant city resources to regional projects.",
                "population_change": 4,
                "budget_change": -9,
                "approval_change": 6,
                "infrastructure_change": 9
            },
            {
                "choice_description": "Join selected projects that directly benefit the city.",
                "population_change": 2,
                "budget_change": -4,
                "approval_change": 4,
                "infrastructure_change": 5
            },
            {
                "choice_description": "Reject the partnership and maintain complete local control over city policy.",
                "population_change": -1,
                "budget_change": 3,
                "approval_change": -4,
                "infrastructure_change": -2
            }
        ]
    },
    {
        "event_description": "A leaked government report reveals that your administration has been warned about several city problems that remain unresolved.",
        "choices": [
            {
                "choice_description": "Accept responsibility and launch an immediate effort to address the problems identified in the report.",
                "population_change": 1,
                "budget_change": -10,
                "approval_change": 7,
                "infrastructure_change": 7
            },
            {
                "choice_description": "Release the full report and create a gradual plan to address its recommendations.",
                "population_change": 0,
                "budget_change": -4,
                "approval_change": 4,
                "infrastructure_change": 3
            },
            {
                "choice_description": "Question the report's conclusions and accuse critics of misrepresenting your administration.",
                "population_change": -2,
                "budget_change": 2,
                "approval_change": -10,
                "infrastructure_change": -3
            }
        ]
    },
    {
        "event_description": "Public opinion polls show growing dissatisfaction with your administration, and political opponents are gaining support.",
        "choices": [
            {
                "choice_description": "Launch a major public outreach campaign and hold meetings across the city.",
                "population_change": 1,
                "budget_change": -8,
                "approval_change": 9,
                "infrastructure_change": 0
            },
            {
                "choice_description": "Focus on improving city services and allow results to rebuild public trust.",
                "population_change": 1,
                "budget_change": -4,
                "approval_change": 5,
                "infrastructure_change": 4
            },
            {
                "choice_description": "Ignore the polls and continue pursuing your administration's existing priorities.",
                "population_change": -1,
                "budget_change": 2,
                "approval_change": -7,
                "infrastructure_change": 0
            }
        ]
    },
    {
        "event_description": "City employees threaten to strike after negotiations over wages and working conditions break down.",
        "choices": [
            {
                "choice_description": "Accept most of the employees' demands and approve a major compensation increase.",
                "population_change": 1,
                "budget_change": -13,
                "approval_change": 8,
                "infrastructure_change": 3
            },
            {
                "choice_description": "Negotiate a compromise with smaller raises and gradual workplace improvements.",
                "population_change": 0,
                "budget_change": -6,
                "approval_change": 5,
                "infrastructure_change": 2
            },
            {
                "choice_description": "Reject the demands and prepare the city to operate during a strike.",
                "population_change": -3,
                "budget_change": 4,
                "approval_change": -10,
                "infrastructure_change": -5
            }
        ]
    },
    {
        "event_description": "A powerful group of business leaders offers to publicly support your administration in exchange for greater influence over city policy.",
        "choices": [
            {
                "choice_description": "Accept their support and give business leaders a larger role in shaping economic policy.",
                "population_change": 2,
                "budget_change": 8,
                "approval_change": -8,
                "infrastructure_change": 3
            },
            {
                "choice_description": "Meet with the group but refuse to offer special political influence.",
                "population_change": 1,
                "budget_change": 2,
                "approval_change": 4,
                "infrastructure_change": 1
            },
            {
                "choice_description": "Publicly reject the offer and criticize attempts to influence city government.",
                "population_change": 0,
                "budget_change": -3,
                "approval_change": 8,
                "infrastructure_change": 0
            }
        ]
    },
    {
        "event_description": "Residents launch a petition demanding a citywide vote on one of your administration's most controversial policies.",
        "choices": [
            {
                "choice_description": "Support the public vote and allow residents to decide the policy's future.",
                "population_change": 1,
                "budget_change": -4,
                "approval_change": 8,
                "infrastructure_change": 0
            },
            {
                "choice_description": "Ask the city council to review and revise the policy before holding a vote.",
                "population_change": 0,
                "budget_change": -2,
                "approval_change": 4,
                "infrastructure_change": 1
            },
            {
                "choice_description": "Oppose the vote and defend the administration's authority to make the decision.",
                "population_change": -2,
                "budget_change": 1,
                "approval_change": -9,
                "infrastructure_change": 0
            }
        ]
    },
    {
        "event_description": "A national news organization publishes a major report evaluating your leadership and the condition of the city.",
        "choices": [
            {
                "choice_description": "Use the attention to promote the city's successes and announce ambitious new goals.",
                "population_change": 4,
                "budget_change": -7,
                "approval_change": 8,
                "infrastructure_change": 3
            },
            {
                "choice_description": "Acknowledge the city's remaining challenges and present a realistic plan for improvement.",
                "population_change": 2,
                "budget_change": -4,
                "approval_change": 6,
                "infrastructure_change": 4
            },
            {
                "choice_description": "Dismiss the report and accuse the news organization of unfairly criticizing the city.",
                "population_change": -2,
                "budget_change": 2,
                "approval_change": -10,
                "infrastructure_change": 0
            }
        ]
    }
]