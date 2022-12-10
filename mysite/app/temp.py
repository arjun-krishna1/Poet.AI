import re
from text_processing import get_phrase_timestamps

resp_data = {
  "text": "Two roads diverged in a yellow wood and sorry I could not travel both and be one traveler long. I stood and looked down as far as I could to where it bent in the undergrowth, then took the other. As just as fair and having perhaps the better claim because it was grassy and wanted wear the last for that the passing there had warned them really about the same. And both that morning equally lay and leaves. No step had trodden black. Oh, I kept the first for another day yet knowing how way leads on to way, I doubt it. If I should ever come back, I shall be telling this with a sigh. Somewhere ages and ages hence two roads diverge in a wood and I I took the one less traveled by and that has made all the difference.",
	"words": [
		{
			"text": "Two",
			"start": 1450,
			"end": 1662,
			"confidence": 1.0,
			"speaker": "A"
		},
		{
			"text": "roads",
			"start": 1716,
			"end": 2234,
			"confidence": 0.84951,
			"speaker": "A"
		},
		{
			"text": "diverged",
			"start": 2282,
			"end": 2986,
			"confidence": 0.39114,
			"speaker": "A"
		},
		{
			"text": "in",
			"start": 3018,
			"end": 3166,
			"confidence": 0.99,
			"speaker": "A"
		},
		{
			"text": "a",
			"start": 3188,
			"end": 3278,
			"confidence": 0.88,
			"speaker": "A"
		},
		{
			"text": "yellow",
			"start": 3284,
			"end": 3626,
			"confidence": 0.65169,
			"speaker": "A"
		},
		{
			"text": "wood",
			"start": 3658,
			"end": 4330,
			"confidence": 0.99831,
			"speaker": "A"
		},
		{
			"text": "and",
			"start": 4490,
			"end": 4910,
			"confidence": 0.57,
			"speaker": "A"
		},
		{
			"text": "sorry",
			"start": 4980,
			"end": 5310,
			"confidence": 0.99642,
			"speaker": "A"
		},
		{
			"text": "I",
			"start": 5380,
			"end": 5566,
			"confidence": 1.0,
			"speaker": "A"
		},
		{
			"text": "could",
			"start": 5588,
			"end": 5726,
			"confidence": 0.99306,
			"speaker": "A"
		},
		{
			"text": "not",
			"start": 5748,
			"end": 5934,
			"confidence": 0.98,
			"speaker": "A"
		},
		{
			"text": "travel",
			"start": 5972,
			"end": 6318,
			"confidence": 0.99988,
			"speaker": "A"
		},
		{
			"text": "both",
			"start": 6404,
			"end": 6894,
			"confidence": 0.99994,
			"speaker": "A"
		},
		{
			"text": "and",
			"start": 7012,
			"end": 7294,
			"confidence": 1.0,
			"speaker": "A"
		},
		{
			"text": "be",
			"start": 7332,
			"end": 7534,
			"confidence": 1.0,
			"speaker": "A"
		},
		{
			"text": "one",
			"start": 7572,
			"end": 7774,
			"confidence": 1.0,
			"speaker": "A"
		},
		{
			"text": "traveler",
			"start": 7812,
			"end": 8682,
			"confidence": 0.8685,
			"speaker": "A"
		},
		{
			"text": "long.",
			"start": 8826,
			"end": 9134,
			"confidence": 0.98549,
			"speaker": "A"
		},
		{
			"text": "I",
			"start": 9172,
			"end": 9374,
			"confidence": 0.53,
			"speaker": "A"
		},
		{
			"text": "stood",
			"start": 9412,
			"end": 10138,
			"confidence": 0.99963,
			"speaker": "A"
		},
		{
			"text": "and",
			"start": 10314,
			"end": 10702,
			"confidence": 0.97,
			"speaker": "A"
		},
		{
			"text": "looked",
			"start": 10756,
			"end": 11022,
			"confidence": 0.99494,
			"speaker": "A"
		},
		{
			"text": "down",
			"start": 11076,
			"end": 11534,
			"confidence": 0.99967,
			"speaker": "A"
		},
		{
			"text": "as",
			"start": 11652,
			"end": 11886,
			"confidence": 0.99966,
			"speaker": "A"
		},
		{
			"text": "far",
			"start": 11908,
			"end": 12094,
			"confidence": 0.98146,
			"speaker": "A"
		},
		{
			"text": "as",
			"start": 12132,
			"end": 12286,
			"confidence": 0.99744,
			"speaker": "A"
		},
		{
			"text": "I",
			"start": 12308,
			"end": 12446,
			"confidence": 1.0,
			"speaker": "A"
		},
		{
			"text": "could",
			"start": 12468,
			"end": 12942,
			"confidence": 0.89646,
			"speaker": "A"
		},
		{
			"text": "to",
			"start": 13076,
			"end": 13374,
			"confidence": 0.52,
			"speaker": "A"
		},
		{
			"text": "where",
			"start": 13412,
			"end": 13614,
			"confidence": 0.97495,
			"speaker": "A"
		},
		{
			"text": "it",
			"start": 13652,
			"end": 13806,
			"confidence": 0.96,
			"speaker": "A"
		},
		{
			"text": "bent",
			"start": 13828,
			"end": 14202,
			"confidence": 0.97281,
			"speaker": "A"
		},
		{
			"text": "in",
			"start": 14266,
			"end": 14446,
			"confidence": 0.99,
			"speaker": "A"
		},
		{
			"text": "the",
			"start": 14468,
			"end": 14606,
			"confidence": 0.97,
			"speaker": "A"
		},
		{
			"text": "undergrowth,",
			"start": 14628,
			"end": 15710,
			"confidence": 0.77138,
			"speaker": "A"
		},
		{
			"text": "then",
			"start": 16130,
			"end": 16494,
			"confidence": 0.85157,
			"speaker": "A"
		},
		{
			"text": "took",
			"start": 16532,
			"end": 16782,
			"confidence": 0.75975,
			"speaker": "A"
		},
		{
			"text": "the",
			"start": 16836,
			"end": 17006,
			"confidence": 1.0,
			"speaker": "A"
		},
		{
			"text": "other.",
			"start": 17028,
			"end": 17454,
			"confidence": 0.99967,
			"speaker": "A"
		},
		{
			"text": "As",
			"start": 17572,
			"end": 17854,
			"confidence": 0.99409,
			"speaker": "A"
		},
		{
			"text": "just",
			"start": 17892,
			"end": 18142,
			"confidence": 0.71148,
			"speaker": "A"
		},
		{
			"text": "as",
			"start": 18196,
			"end": 18414,
			"confidence": 0.92925,
			"speaker": "A"
		},
		{
			"text": "fair",
			"start": 18452,
			"end": 18990,
			"confidence": 0.98542,
			"speaker": "A"
		},
		{
			"text": "and",
			"start": 19140,
			"end": 19502,
			"confidence": 0.7,
			"speaker": "A"
		},
		{
			"text": "having",
			"start": 19556,
			"end": 19870,
			"confidence": 0.99938,
			"speaker": "A"
		},
		{
			"text": "perhaps",
			"start": 19940,
			"end": 20314,
			"confidence": 0.9695,
			"speaker": "A"
		},
		{
			"text": "the",
			"start": 20362,
			"end": 20526,
			"confidence": 0.53,
			"speaker": "A"
		},
		{
			"text": "better",
			"start": 20548,
			"end": 20830,
			"confidence": 0.99988,
			"speaker": "A"
		},
		{
			"text": "claim",
			"start": 20900,
			"end": 21466,
			"confidence": 0.99879,
			"speaker": "A"
		},
		{
			"text": "because",
			"start": 21578,
			"end": 22046,
			"confidence": 0.99972,
			"speaker": "A"
		},
		{
			"text": "it",
			"start": 22148,
			"end": 22366,
			"confidence": 1.0,
			"speaker": "A"
		},
		{
			"text": "was",
			"start": 22388,
			"end": 22670,
			"confidence": 0.93955,
			"speaker": "A"
		},
		{
			"text": "grassy",
			"start": 22740,
			"end": 23226,
			"confidence": 0.99328,
			"speaker": "A"
		},
		{
			"text": "and",
			"start": 23258,
			"end": 23358,
			"confidence": 0.99,
			"speaker": "A"
		},
		{
			"text": "wanted",
			"start": 23364,
			"end": 23630,
			"confidence": 0.95589,
			"speaker": "A"
		},
		{
			"text": "wear",
			"start": 23700,
			"end": 24430,
			"confidence": 0.83156,
			"speaker": "A"
		},
		{
			"text": "the",
			"start": 24810,
			"end": 25126,
			"confidence": 0.83,
			"speaker": "A"
		},
		{
			"text": "last",
			"start": 25148,
			"end": 25334,
			"confidence": 0.99783,
			"speaker": "A"
		},
		{
			"text": "for",
			"start": 25372,
			"end": 25622,
			"confidence": 0.97774,
			"speaker": "A"
		},
		{
			"text": "that",
			"start": 25676,
			"end": 26038,
			"confidence": 1.0,
			"speaker": "A"
		},
		{
			"text": "the",
			"start": 26124,
			"end": 26374,
			"confidence": 1.0,
			"speaker": "A"
		},
		{
			"text": "passing",
			"start": 26412,
			"end": 26882,
			"confidence": 0.95753,
			"speaker": "A"
		},
		{
			"text": "there",
			"start": 26946,
			"end": 27414,
			"confidence": 0.99946,
			"speaker": "A"
		},
		{
			"text": "had",
			"start": 27532,
			"end": 27814,
			"confidence": 0.99983,
			"speaker": "A"
		},
		{
			"text": "warned",
			"start": 27852,
			"end": 28146,
			"confidence": 0.71489,
			"speaker": "A"
		},
		{
			"text": "them",
			"start": 28178,
			"end": 28374,
			"confidence": 0.99937,
			"speaker": "A"
		},
		{
			"text": "really",
			"start": 28412,
			"end": 28662,
			"confidence": 0.99923,
			"speaker": "A"
		},
		{
			"text": "about",
			"start": 28716,
			"end": 28982,
			"confidence": 0.99968,
			"speaker": "A"
		},
		{
			"text": "the",
			"start": 29036,
			"end": 29206,
			"confidence": 1.0,
			"speaker": "A"
		},
		{
			"text": "same.",
			"start": 29228,
			"end": 29800,
			"confidence": 0.99832,
			"speaker": "A"
		},
		{
			"text": "And",
			"start": 30250,
			"end": 30662,
			"confidence": 0.94,
			"speaker": "A"
		},
		{
			"text": "both",
			"start": 30716,
			"end": 30982,
			"confidence": 0.9996,
			"speaker": "A"
		},
		{
			"text": "that",
			"start": 31036,
			"end": 31302,
			"confidence": 0.77,
			"speaker": "A"
		},
		{
			"text": "morning",
			"start": 31356,
			"end": 31766,
			"confidence": 0.99975,
			"speaker": "A"
		},
		{
			"text": "equally",
			"start": 31868,
			"end": 32322,
			"confidence": 0.86406,
			"speaker": "A"
		},
		{
			"text": "lay",
			"start": 32386,
			"end": 32902,
			"confidence": 0.99417,
			"speaker": "A"
		},
		{
			"text": "and",
			"start": 33036,
			"end": 33334,
			"confidence": 0.53,
			"speaker": "A"
		},
		{
			"text": "leaves.",
			"start": 33372,
			"end": 33746,
			"confidence": 0.54031,
			"speaker": "A"
		},
		{
			"text": "No",
			"start": 33778,
			"end": 33974,
			"confidence": 1.0,
			"speaker": "A"
		},
		{
			"text": "step",
			"start": 34012,
			"end": 34310,
			"confidence": 0.99849,
			"speaker": "A"
		},
		{
			"text": "had",
			"start": 34380,
			"end": 34566,
			"confidence": 0.98321,
			"speaker": "A"
		},
		{
			"text": "trodden",
			"start": 34588,
			"end": 35026,
			"confidence": 0.53886,
			"speaker": "A"
		},
		{
			"text": "black.",
			"start": 35058,
			"end": 35686,
			"confidence": 0.99825,
			"speaker": "A"
		},
		{
			"text": "Oh,",
			"start": 35868,
			"end": 36406,
			"confidence": 1.0,
			"speaker": "A"
		},
		{
			"text": "I",
			"start": 36508,
			"end": 36726,
			"confidence": 1.0,
			"speaker": "A"
		},
		{
			"text": "kept",
			"start": 36748,
			"end": 36994,
			"confidence": 0.99987,
			"speaker": "A"
		},
		{
			"text": "the",
			"start": 37042,
			"end": 37206,
			"confidence": 1.0,
			"speaker": "A"
		},
		{
			"text": "first",
			"start": 37228,
			"end": 37510,
			"confidence": 0.99,
			"speaker": "A"
		},
		{
			"text": "for",
			"start": 37580,
			"end": 37814,
			"confidence": 0.99997,
			"speaker": "A"
		},
		{
			"text": "another",
			"start": 37852,
			"end": 38102,
			"confidence": 0.99997,
			"speaker": "A"
		},
		{
			"text": "day",
			"start": 38156,
			"end": 38760,
			"confidence": 0.99966,
			"speaker": "A"
		},
		{
			"text": "yet",
			"start": 39450,
			"end": 39862,
			"confidence": 0.99996,
			"speaker": "A"
		},
		{
			"text": "knowing",
			"start": 39916,
			"end": 40274,
			"confidence": 0.99987,
			"speaker": "A"
		},
		{
			"text": "how",
			"start": 40322,
			"end": 40726,
			"confidence": 1.0,
			"speaker": "A"
		},
		{
			"text": "way",
			"start": 40828,
			"end": 41142,
			"confidence": 0.76764,
			"speaker": "A"
		},
		{
			"text": "leads",
			"start": 41196,
			"end": 41506,
			"confidence": 0.99969,
			"speaker": "A"
		},
		{
			"text": "on",
			"start": 41538,
			"end": 41686,
			"confidence": 0.99979,
			"speaker": "A"
		},
		{
			"text": "to",
			"start": 41708,
			"end": 41846,
			"confidence": 0.82,
			"speaker": "A"
		},
		{
			"text": "way,",
			"start": 41868,
			"end": 42294,
			"confidence": 0.69049,
			"speaker": "A"
		},
		{
			"text": "I",
			"start": 42412,
			"end": 42694,
			"confidence": 0.84,
			"speaker": "A"
		},
		{
			"text": "doubt",
			"start": 42732,
			"end": 42978,
			"confidence": 0.89199,
			"speaker": "A"
		},
		{
			"text": "it.",
			"start": 42994,
			"end": 43174,
			"confidence": 0.92,
			"speaker": "A"
		},
		{
			"text": "If",
			"start": 43212,
			"end": 43366,
			"confidence": 0.99999,
			"speaker": "A"
		},
		{
			"text": "I",
			"start": 43388,
			"end": 43526,
			"confidence": 0.54,
			"speaker": "A"
		},
		{
			"text": "should",
			"start": 43548,
			"end": 43734,
			"confidence": 0.99997,
			"speaker": "A"
		},
		{
			"text": "ever",
			"start": 43772,
			"end": 43974,
			"confidence": 0.99985,
			"speaker": "A"
		},
		{
			"text": "come",
			"start": 44012,
			"end": 44214,
			"confidence": 0.99998,
			"speaker": "A"
		},
		{
			"text": "back,",
			"start": 44252,
			"end": 44840,
			"confidence": 0.99976,
			"speaker": "A"
		},
		{
			"text": "I",
			"start": 45370,
			"end": 45686,
			"confidence": 1.0,
			"speaker": "A"
		},
		{
			"text": "shall",
			"start": 45708,
			"end": 45906,
			"confidence": 0.99771,
			"speaker": "A"
		},
		{
			"text": "be",
			"start": 45938,
			"end": 46086,
			"confidence": 1.0,
			"speaker": "A"
		},
		{
			"text": "telling",
			"start": 46108,
			"end": 46386,
			"confidence": 0.98045,
			"speaker": "A"
		},
		{
			"text": "this",
			"start": 46418,
			"end": 46614,
			"confidence": 0.99972,
			"speaker": "A"
		},
		{
			"text": "with",
			"start": 46652,
			"end": 46854,
			"confidence": 0.99805,
			"speaker": "A"
		},
		{
			"text": "a",
			"start": 46892,
			"end": 47286,
			"confidence": 0.34,
			"speaker": "A"
		},
		{
			"text": "sigh.",
			"start": 47388,
			"end": 48130,
			"confidence": 0.41729,
			"speaker": "A"
		},
		{
			"text": "Somewhere",
			"start": 48290,
			"end": 48834,
			"confidence": 0.12841,
			"speaker": "A"
		},
		{
			"text": "ages",
			"start": 48882,
			"end": 49266,
			"confidence": 0.99331,
			"speaker": "A"
		},
		{
			"text": "and",
			"start": 49298,
			"end": 49398,
			"confidence": 0.93,
			"speaker": "A"
		},
		{
			"text": "ages",
			"start": 49404,
			"end": 49698,
			"confidence": 0.97106,
			"speaker": "A"
		},
		{
			"text": "hence",
			"start": 49714,
			"end": 50442,
			"confidence": 0.38661,
			"speaker": "A"
		},
		{
			"text": "two",
			"start": 50626,
			"end": 50974,
			"confidence": 0.99,
			"speaker": "A"
		},
		{
			"text": "roads",
			"start": 51012,
			"end": 51466,
			"confidence": 0.65274,
			"speaker": "A"
		},
		{
			"text": "diverge",
			"start": 51498,
			"end": 51978,
			"confidence": 0.60676,
			"speaker": "A"
		},
		{
			"text": "in",
			"start": 51994,
			"end": 52126,
			"confidence": 1.0,
			"speaker": "A"
		},
		{
			"text": "a",
			"start": 52148,
			"end": 52238,
			"confidence": 0.99,
			"speaker": "A"
		},
		{
			"text": "wood",
			"start": 52244,
			"end": 52746,
			"confidence": 0.99289,
			"speaker": "A"
		},
		{
			"text": "and",
			"start": 52858,
			"end": 53134,
			"confidence": 0.99,
			"speaker": "A"
		},
		{
			"text": "I",
			"start": 53172,
			"end": 53710,
			"confidence": 0.56,
			"speaker": "A"
		},
		{
			"text": "I",
			"start": 53860,
			"end": 54174,
			"confidence": 0.54,
			"speaker": "A"
		},
		{
			"text": "took",
			"start": 54212,
			"end": 54414,
			"confidence": 0.99978,
			"speaker": "A"
		},
		{
			"text": "the",
			"start": 54452,
			"end": 54606,
			"confidence": 0.99,
			"speaker": "A"
		},
		{
			"text": "one",
			"start": 54628,
			"end": 54814,
			"confidence": 1.0,
			"speaker": "A"
		},
		{
			"text": "less",
			"start": 54852,
			"end": 55054,
			"confidence": 0.50789,
			"speaker": "A"
		},
		{
			"text": "traveled",
			"start": 55092,
			"end": 55498,
			"confidence": 0.70088,
			"speaker": "A"
		},
		{
			"text": "by",
			"start": 55514,
			"end": 56174,
			"confidence": 0.75957,
			"speaker": "A"
		},
		{
			"text": "and",
			"start": 56372,
			"end": 56686,
			"confidence": 1.0,
			"speaker": "A"
		},
		{
			"text": "that",
			"start": 56708,
			"end": 56846,
			"confidence": 1.0,
			"speaker": "A"
		},
		{
			"text": "has",
			"start": 56868,
			"end": 57054,
			"confidence": 0.66163,
			"speaker": "A"
		},
		{
			"text": "made",
			"start": 57092,
			"end": 57486,
			"confidence": 0.9998,
			"speaker": "A"
		},
		{
			"text": "all",
			"start": 57588,
			"end": 57806,
			"confidence": 1.0,
			"speaker": "A"
		},
		{
			"text": "the",
			"start": 57828,
			"end": 58014,
			"confidence": 0.84,
			"speaker": "A"
		},
		{
			"text": "difference.",
			"start": 58052,
			"end": 58140,
			"confidence": 0.99964,
			"speaker": "A"
		}
	],
	"utterances": [
		{
			"confidence": 0.8946829166666667,
			"end": 58140,
			"speaker": "A",
			"start": 1450,
			"text": "Two roads diverged in a yellow wood and sorry I could not travel both and be one traveler long. I stood and looked down as far as I could to where it bent in the undergrowth, then took the other. As just as fair and having perhaps the better claim because it was grassy and wanted wear the last for that the passing there had warned them really about the same. And both that morning equally lay and leaves. No step had trodden black. Oh, I kept the first for another day yet knowing how way leads on to way, I doubt it. If I should ever come back, I shall be telling this with a sigh. Somewhere ages and ages hence two roads diverge in a wood and I I took the one less traveled by and that has made all the difference.",
			"words": [
				{
					"text": "Two",
					"start": 1450,
					"end": 1662,
					"confidence": 1.0,
					"speaker": "A"
				},
				{
					"text": "roads",
					"start": 1716,
					"end": 2234,
					"confidence": 0.84951,
					"speaker": "A"
				},
				{
					"text": "diverged",
					"start": 2282,
					"end": 2986,
					"confidence": 0.39114,
					"speaker": "A"
				},
				{
					"text": "in",
					"start": 3018,
					"end": 3166,
					"confidence": 0.99,
					"speaker": "A"
				},
				{
					"text": "a",
					"start": 3188,
					"end": 3278,
					"confidence": 0.88,
					"speaker": "A"
				},
				{
					"text": "yellow",
					"start": 3284,
					"end": 3626,
					"confidence": 0.65169,
					"speaker": "A"
				},
				{
					"text": "wood",
					"start": 3658,
					"end": 4330,
					"confidence": 0.99831,
					"speaker": "A"
				},
				{
					"text": "and",
					"start": 4490,
					"end": 4910,
					"confidence": 0.57,
					"speaker": "A"
				},
				{
					"text": "sorry",
					"start": 4980,
					"end": 5310,
					"confidence": 0.99642,
					"speaker": "A"
				},
				{
					"text": "I",
					"start": 5380,
					"end": 5566,
					"confidence": 1.0,
					"speaker": "A"
				},
				{
					"text": "could",
					"start": 5588,
					"end": 5726,
					"confidence": 0.99306,
					"speaker": "A"
				},
				{
					"text": "not",
					"start": 5748,
					"end": 5934,
					"confidence": 0.98,
					"speaker": "A"
				},
				{
					"text": "travel",
					"start": 5972,
					"end": 6318,
					"confidence": 0.99988,
					"speaker": "A"
				},
				{
					"text": "both",
					"start": 6404,
					"end": 6894,
					"confidence": 0.99994,
					"speaker": "A"
				},
				{
					"text": "and",
					"start": 7012,
					"end": 7294,
					"confidence": 1.0,
					"speaker": "A"
				},
				{
					"text": "be",
					"start": 7332,
					"end": 7534,
					"confidence": 1.0,
					"speaker": "A"
				},
				{
					"text": "one",
					"start": 7572,
					"end": 7774,
					"confidence": 1.0,
					"speaker": "A"
				},
				{
					"text": "traveler",
					"start": 7812,
					"end": 8682,
					"confidence": 0.8685,
					"speaker": "A"
				},
				{
					"text": "long.",
					"start": 8826,
					"end": 9134,
					"confidence": 0.98549,
					"speaker": "A"
				},
				{
					"text": "I",
					"start": 9172,
					"end": 9374,
					"confidence": 0.53,
					"speaker": "A"
				},
				{
					"text": "stood",
					"start": 9412,
					"end": 10138,
					"confidence": 0.99963,
					"speaker": "A"
				},
				{
					"text": "and",
					"start": 10314,
					"end": 10702,
					"confidence": 0.97,
					"speaker": "A"
				},
				{
					"text": "looked",
					"start": 10756,
					"end": 11022,
					"confidence": 0.99494,
					"speaker": "A"
				},
				{
					"text": "down",
					"start": 11076,
					"end": 11534,
					"confidence": 0.99967,
					"speaker": "A"
				},
				{
					"text": "as",
					"start": 11652,
					"end": 11886,
					"confidence": 0.99966,
					"speaker": "A"
				},
				{
					"text": "far",
					"start": 11908,
					"end": 12094,
					"confidence": 0.98146,
					"speaker": "A"
				},
				{
					"text": "as",
					"start": 12132,
					"end": 12286,
					"confidence": 0.99744,
					"speaker": "A"
				},
				{
					"text": "I",
					"start": 12308,
					"end": 12446,
					"confidence": 1.0,
					"speaker": "A"
				},
				{
					"text": "could",
					"start": 12468,
					"end": 12942,
					"confidence": 0.89646,
					"speaker": "A"
				},
				{
					"text": "to",
					"start": 13076,
					"end": 13374,
					"confidence": 0.52,
					"speaker": "A"
				},
				{
					"text": "where",
					"start": 13412,
					"end": 13614,
					"confidence": 0.97495,
					"speaker": "A"
				},
				{
					"text": "it",
					"start": 13652,
					"end": 13806,
					"confidence": 0.96,
					"speaker": "A"
				},
				{
					"text": "bent",
					"start": 13828,
					"end": 14202,
					"confidence": 0.97281,
					"speaker": "A"
				},
				{
					"text": "in",
					"start": 14266,
					"end": 14446,
					"confidence": 0.99,
					"speaker": "A"
				},
				{
					"text": "the",
					"start": 14468,
					"end": 14606,
					"confidence": 0.97,
					"speaker": "A"
				},
				{
					"text": "undergrowth,",
					"start": 14628,
					"end": 15710,
					"confidence": 0.77138,
					"speaker": "A"
				},
				{
					"text": "then",
					"start": 16130,
					"end": 16494,
					"confidence": 0.85157,
					"speaker": "A"
				},
				{
					"text": "took",
					"start": 16532,
					"end": 16782,
					"confidence": 0.75975,
					"speaker": "A"
				},
				{
					"text": "the",
					"start": 16836,
					"end": 17006,
					"confidence": 1.0,
					"speaker": "A"
				},
				{
					"text": "other.",
					"start": 17028,
					"end": 17454,
					"confidence": 0.99967,
					"speaker": "A"
				},
				{
					"text": "As",
					"start": 17572,
					"end": 17854,
					"confidence": 0.99409,
					"speaker": "A"
				},
				{
					"text": "just",
					"start": 17892,
					"end": 18142,
					"confidence": 0.71148,
					"speaker": "A"
				},
				{
					"text": "as",
					"start": 18196,
					"end": 18414,
					"confidence": 0.92925,
					"speaker": "A"
				},
				{
					"text": "fair",
					"start": 18452,
					"end": 18990,
					"confidence": 0.98542,
					"speaker": "A"
				},
				{
					"text": "and",
					"start": 19140,
					"end": 19502,
					"confidence": 0.7,
					"speaker": "A"
				},
				{
					"text": "having",
					"start": 19556,
					"end": 19870,
					"confidence": 0.99938,
					"speaker": "A"
				},
				{
					"text": "perhaps",
					"start": 19940,
					"end": 20314,
					"confidence": 0.9695,
					"speaker": "A"
				},
				{
					"text": "the",
					"start": 20362,
					"end": 20526,
					"confidence": 0.53,
					"speaker": "A"
				},
				{
					"text": "better",
					"start": 20548,
					"end": 20830,
					"confidence": 0.99988,
					"speaker": "A"
				},
				{
					"text": "claim",
					"start": 20900,
					"end": 21466,
					"confidence": 0.99879,
					"speaker": "A"
				},
				{
					"text": "because",
					"start": 21578,
					"end": 22046,
					"confidence": 0.99972,
					"speaker": "A"
				},
				{
					"text": "it",
					"start": 22148,
					"end": 22366,
					"confidence": 1.0,
					"speaker": "A"
				},
				{
					"text": "was",
					"start": 22388,
					"end": 22670,
					"confidence": 0.93955,
					"speaker": "A"
				},
				{
					"text": "grassy",
					"start": 22740,
					"end": 23226,
					"confidence": 0.99328,
					"speaker": "A"
				},
				{
					"text": "and",
					"start": 23258,
					"end": 23358,
					"confidence": 0.99,
					"speaker": "A"
				},
				{
					"text": "wanted",
					"start": 23364,
					"end": 23630,
					"confidence": 0.95589,
					"speaker": "A"
				},
				{
					"text": "wear",
					"start": 23700,
					"end": 24430,
					"confidence": 0.83156,
					"speaker": "A"
				},
				{
					"text": "the",
					"start": 24810,
					"end": 25126,
					"confidence": 0.83,
					"speaker": "A"
				},
				{
					"text": "last",
					"start": 25148,
					"end": 25334,
					"confidence": 0.99783,
					"speaker": "A"
				},
				{
					"text": "for",
					"start": 25372,
					"end": 25622,
					"confidence": 0.97774,
					"speaker": "A"
				},
				{
					"text": "that",
					"start": 25676,
					"end": 26038,
					"confidence": 1.0,
					"speaker": "A"
				},
				{
					"text": "the",
					"start": 26124,
					"end": 26374,
					"confidence": 1.0,
					"speaker": "A"
				},
				{
					"text": "passing",
					"start": 26412,
					"end": 26882,
					"confidence": 0.95753,
					"speaker": "A"
				},
				{
					"text": "there",
					"start": 26946,
					"end": 27414,
					"confidence": 0.99946,
					"speaker": "A"
				},
				{
					"text": "had",
					"start": 27532,
					"end": 27814,
					"confidence": 0.99983,
					"speaker": "A"
				},
				{
					"text": "warned",
					"start": 27852,
					"end": 28146,
					"confidence": 0.71489,
					"speaker": "A"
				},
				{
					"text": "them",
					"start": 28178,
					"end": 28374,
					"confidence": 0.99937,
					"speaker": "A"
				},
				{
					"text": "really",
					"start": 28412,
					"end": 28662,
					"confidence": 0.99923,
					"speaker": "A"
				},
				{
					"text": "about",
					"start": 28716,
					"end": 28982,
					"confidence": 0.99968,
					"speaker": "A"
				},
				{
					"text": "the",
					"start": 29036,
					"end": 29206,
					"confidence": 1.0,
					"speaker": "A"
				},
				{
					"text": "same.",
					"start": 29228,
					"end": 29800,
					"confidence": 0.99832,
					"speaker": "A"
				},
				{
					"text": "And",
					"start": 30250,
					"end": 30662,
					"confidence": 0.94,
					"speaker": "A"
				},
				{
					"text": "both",
					"start": 30716,
					"end": 30982,
					"confidence": 0.9996,
					"speaker": "A"
				},
				{
					"text": "that",
					"start": 31036,
					"end": 31302,
					"confidence": 0.77,
					"speaker": "A"
				},
				{
					"text": "morning",
					"start": 31356,
					"end": 31766,
					"confidence": 0.99975,
					"speaker": "A"
				},
				{
					"text": "equally",
					"start": 31868,
					"end": 32322,
					"confidence": 0.86406,
					"speaker": "A"
				},
				{
					"text": "lay",
					"start": 32386,
					"end": 32902,
					"confidence": 0.99417,
					"speaker": "A"
				},
				{
					"text": "and",
					"start": 33036,
					"end": 33334,
					"confidence": 0.53,
					"speaker": "A"
				},
				{
					"text": "leaves.",
					"start": 33372,
					"end": 33746,
					"confidence": 0.54031,
					"speaker": "A"
				},
				{
					"text": "No",
					"start": 33778,
					"end": 33974,
					"confidence": 1.0,
					"speaker": "A"
				},
				{
					"text": "step",
					"start": 34012,
					"end": 34310,
					"confidence": 0.99849,
					"speaker": "A"
				},
				{
					"text": "had",
					"start": 34380,
					"end": 34566,
					"confidence": 0.98321,
					"speaker": "A"
				},
				{
					"text": "trodden",
					"start": 34588,
					"end": 35026,
					"confidence": 0.53886,
					"speaker": "A"
				},
				{
					"text": "black.",
					"start": 35058,
					"end": 35686,
					"confidence": 0.99825,
					"speaker": "A"
				},
				{
					"text": "Oh,",
					"start": 35868,
					"end": 36406,
					"confidence": 1.0,
					"speaker": "A"
				},
				{
					"text": "I",
					"start": 36508,
					"end": 36726,
					"confidence": 1.0,
					"speaker": "A"
				},
				{
					"text": "kept",
					"start": 36748,
					"end": 36994,
					"confidence": 0.99987,
					"speaker": "A"
				},
				{
					"text": "the",
					"start": 37042,
					"end": 37206,
					"confidence": 1.0,
					"speaker": "A"
				},
				{
					"text": "first",
					"start": 37228,
					"end": 37510,
					"confidence": 0.99,
					"speaker": "A"
				},
				{
					"text": "for",
					"start": 37580,
					"end": 37814,
					"confidence": 0.99997,
					"speaker": "A"
				},
				{
					"text": "another",
					"start": 37852,
					"end": 38102,
					"confidence": 0.99997,
					"speaker": "A"
				},
				{
					"text": "day",
					"start": 38156,
					"end": 38760,
					"confidence": 0.99966,
					"speaker": "A"
				},
				{
					"text": "yet",
					"start": 39450,
					"end": 39862,
					"confidence": 0.99996,
					"speaker": "A"
				},
				{
					"text": "knowing",
					"start": 39916,
					"end": 40274,
					"confidence": 0.99987,
					"speaker": "A"
				},
				{
					"text": "how",
					"start": 40322,
					"end": 40726,
					"confidence": 1.0,
					"speaker": "A"
				},
				{
					"text": "way",
					"start": 40828,
					"end": 41142,
					"confidence": 0.76764,
					"speaker": "A"
				},
				{
					"text": "leads",
					"start": 41196,
					"end": 41506,
					"confidence": 0.99969,
					"speaker": "A"
				},
				{
					"text": "on",
					"start": 41538,
					"end": 41686,
					"confidence": 0.99979,
					"speaker": "A"
				},
				{
					"text": "to",
					"start": 41708,
					"end": 41846,
					"confidence": 0.82,
					"speaker": "A"
				},
				{
					"text": "way,",
					"start": 41868,
					"end": 42294,
					"confidence": 0.69049,
					"speaker": "A"
				},
				{
					"text": "I",
					"start": 42412,
					"end": 42694,
					"confidence": 0.84,
					"speaker": "A"
				},
				{
					"text": "doubt",
					"start": 42732,
					"end": 42978,
					"confidence": 0.89199,
					"speaker": "A"
				},
				{
					"text": "it.",
					"start": 42994,
					"end": 43174,
					"confidence": 0.92,
					"speaker": "A"
				},
				{
					"text": "If",
					"start": 43212,
					"end": 43366,
					"confidence": 0.99999,
					"speaker": "A"
				},
				{
					"text": "I",
					"start": 43388,
					"end": 43526,
					"confidence": 0.54,
					"speaker": "A"
				},
				{
					"text": "should",
					"start": 43548,
					"end": 43734,
					"confidence": 0.99997,
					"speaker": "A"
				},
				{
					"text": "ever",
					"start": 43772,
					"end": 43974,
					"confidence": 0.99985,
					"speaker": "A"
				},
				{
					"text": "come",
					"start": 44012,
					"end": 44214,
					"confidence": 0.99998,
					"speaker": "A"
				},
				{
					"text": "back,",
					"start": 44252,
					"end": 44840,
					"confidence": 0.99976,
					"speaker": "A"
				},
				{
					"text": "I",
					"start": 45370,
					"end": 45686,
					"confidence": 1.0,
					"speaker": "A"
				},
				{
					"text": "shall",
					"start": 45708,
					"end": 45906,
					"confidence": 0.99771,
					"speaker": "A"
				},
				{
					"text": "be",
					"start": 45938,
					"end": 46086,
					"confidence": 1.0,
					"speaker": "A"
				},
				{
					"text": "telling",
					"start": 46108,
					"end": 46386,
					"confidence": 0.98045,
					"speaker": "A"
				},
				{
					"text": "this",
					"start": 46418,
					"end": 46614,
					"confidence": 0.99972,
					"speaker": "A"
				},
				{
					"text": "with",
					"start": 46652,
					"end": 46854,
					"confidence": 0.99805,
					"speaker": "A"
				},
				{
					"text": "a",
					"start": 46892,
					"end": 47286,
					"confidence": 0.34,
					"speaker": "A"
				},
				{
					"text": "sigh.",
					"start": 47388,
					"end": 48130,
					"confidence": 0.41729,
					"speaker": "A"
				},
				{
					"text": "Somewhere",
					"start": 48290,
					"end": 48834,
					"confidence": 0.12841,
					"speaker": "A"
				},
				{
					"text": "ages",
					"start": 48882,
					"end": 49266,
					"confidence": 0.99331,
					"speaker": "A"
				},
				{
					"text": "and",
					"start": 49298,
					"end": 49398,
					"confidence": 0.93,
					"speaker": "A"
				},
				{
					"text": "ages",
					"start": 49404,
					"end": 49698,
					"confidence": 0.97106,
					"speaker": "A"
				},
				{
					"text": "hence",
					"start": 49714,
					"end": 50442,
					"confidence": 0.38661,
					"speaker": "A"
				},
				{
					"text": "two",
					"start": 50626,
					"end": 50974,
					"confidence": 0.99,
					"speaker": "A"
				},
				{
					"text": "roads",
					"start": 51012,
					"end": 51466,
					"confidence": 0.65274,
					"speaker": "A"
				},
				{
					"text": "diverge",
					"start": 51498,
					"end": 51978,
					"confidence": 0.60676,
					"speaker": "A"
				},
				{
					"text": "in",
					"start": 51994,
					"end": 52126,
					"confidence": 1.0,
					"speaker": "A"
				},
				{
					"text": "a",
					"start": 52148,
					"end": 52238,
					"confidence": 0.99,
					"speaker": "A"
				},
				{
					"text": "wood",
					"start": 52244,
					"end": 52746,
					"confidence": 0.99289,
					"speaker": "A"
				},
				{
					"text": "and",
					"start": 52858,
					"end": 53134,
					"confidence": 0.99,
					"speaker": "A"
				},
				{
					"text": "I",
					"start": 53172,
					"end": 53710,
					"confidence": 0.56,
					"speaker": "A"
				},
				{
					"text": "I",
					"start": 53860,
					"end": 54174,
					"confidence": 0.54,
					"speaker": "A"
				},
				{
					"text": "took",
					"start": 54212,
					"end": 54414,
					"confidence": 0.99978,
					"speaker": "A"
				},
				{
					"text": "the",
					"start": 54452,
					"end": 54606,
					"confidence": 0.99,
					"speaker": "A"
				},
				{
					"text": "one",
					"start": 54628,
					"end": 54814,
					"confidence": 1.0,
					"speaker": "A"
				},
				{
					"text": "less",
					"start": 54852,
					"end": 55054,
					"confidence": 0.50789,
					"speaker": "A"
				},
				{
					"text": "traveled",
					"start": 55092,
					"end": 55498,
					"confidence": 0.70088,
					"speaker": "A"
				},
				{
					"text": "by",
					"start": 55514,
					"end": 56174,
					"confidence": 0.75957,
					"speaker": "A"
				},
				{
					"text": "and",
					"start": 56372,
					"end": 56686,
					"confidence": 1.0,
					"speaker": "A"
				},
				{
					"text": "that",
					"start": 56708,
					"end": 56846,
					"confidence": 1.0,
					"speaker": "A"
				},
				{
					"text": "has",
					"start": 56868,
					"end": 57054,
					"confidence": 0.66163,
					"speaker": "A"
				},
				{
					"text": "made",
					"start": 57092,
					"end": 57486,
					"confidence": 0.9998,
					"speaker": "A"
				},
				{
					"text": "all",
					"start": 57588,
					"end": 57806,
					"confidence": 1.0,
					"speaker": "A"
				},
				{
					"text": "the",
					"start": 57828,
					"end": 58014,
					"confidence": 0.84,
					"speaker": "A"
				},
				{
					"text": "difference.",
					"start": 58052,
					"end": 58140,
					"confidence": 0.99964,
					"speaker": "A"
				}
			]
		}
	],
}

print(get_phrase_timestamps(resp_data.get("words")))
