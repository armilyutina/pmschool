from django.shortcuts import render
import json
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt,csrf_protect #Add this
from django.http import HttpResponse
import numpy as np
import copy
import operator


@csrf_protect
# Create your views here.
def direction(request):
	if request.method == 'GET':
		return render(request, 'direction/direction.html')
	if request.method == 'POST':

		mathBlockOne = [9.2, 9.7, 10.2, 9.4, 9.9, 8.3, 9.8, 9.3, 9.5, 5.1, 9.8, 9.8]
		mathBlockTwo = [8.2, 5.3, 8.9, 17.3, 3.8, 10.2, 10.6, 19.5, 10.3, 5.32, 9.2, 11.6]
		phisBlockOne = [32.7, 30.5, 24.01, 7.7, 3.8, 20.04, 10.8, 3.5, 17.5, 5.48, 15.38, 19.4]
		phisBlockTwo = [13.3, 18.3, 7.2, 5.1, 4.8, 17.35, 13.2, 2.9, 14.2, 5.2, 17.01, 17.9]
		phisBlockThree = [13.9, 16.6, 10.9, 14.4, 3.8, 10.01, 5.6, 9.5, 13.3, 5.3, 14.2, 13.72]
		infBlockOne = [7.3, 6.2, 10.6, 17.8, 5.6, 10.9, 9.9, 17.1, 12.2, 5.4, 7.49, 10.4]
		infBlockTwo = [4.5, 8.2, 21.01, 16.2, 10.3, 13.2, 7.9, 28.9, 8.3, 7.9, 10.83, 8.2]
		socialBlockOne = [4.4, 3.3, 4, 7.3, 20.3, 5.5, 4.4, 5.9, 7.7, 36,8, 6, 4.7]
		socialBlockTwo = [6.4, 1.8, 3, 4.8, 37.6, 4.5, 4.5, 3.5, 7, 23.5, 10.1, 4.28]

		xBlock = {'mathBlockOne':mathBlockOne, 'mathBlockTwo':mathBlockTwo, 'phisBlockOne':phisBlockOne, 'phisBlockTwo':phisBlockTwo, 'phisBlockThree':phisBlockThree, 'infBlockOne':infBlockOne, 'infBlockTwo':infBlockTwo, 'socialBlockOne':socialBlockOne, 'socialBlockTwo':socialBlockTwo }

		filteredCriterion = []
		data = json.loads(request.body.decode())
		print(data)
		d = dict(data)
		filteredData = dict()
		for k, v in d.items():
			if v != '' and type(v) != list:
				filteredData[k] = v
				filteredCriterion.append(xBlock[k]) #значения критериев

		print(filteredData)
		m = len(filteredData)
		n = 9
		r = []
		for key, value in filteredData.items():
			criterion = value #min max
			tmpR = []

			for i in range(n):
				if i < m:
					x = filteredCriterion[i]
				tmp = []
				for j in range(n):
					if i != j:
						if criterion == "max":
							tmp.append(x[j] / (x[i] + x[j]))
						else:
							tmp.append(x[i] / (x[i] + x[j]))
					else:
						if x[i] == 0 and x[j] == 0:
							tmp.append(0.5)
						else:
							tmp.append(1)

				tmpR.append(tmp)
			tmpR = np.array(tmpR)

			r.append(tmpR)


		p = np.zeros((n,n), dtype=float)
		for t in range(m):
			p += r[t]


		result = {}
		for i in range(n):
			tmp = 0
			for j in range(n):
				tmp += p[j][i] - p[i][j]
			result[i+1] = tmp

		result = sorted(result.items(), key=operator.itemgetter(1), reverse=True)
		print(result)

		methodResult = []
		for i in range(3):
			methodResult.append(result[i])

		result = {}

		print(methodResult)
		print('\n')
		res = []
		for k, v in methodResult:
			if k == 1:
				res.append("Авиастроение")
			if k == 2:
				res.append("Двигателестроение")
			if k == 3:
				res.append("Бортовая электроника и техническая кибернетика")
			if k == 4:
				res.append("Радиоэлектроника и системы связи")
			if k == 5:
				res.append("Управ.-экономические и лингвитсические направления")
			if k == 6:
				res.append("Ракетно-космические системы")
			if k == 7:
				res.append("Робототехнические системы и комплексы вооружения ЛА")
			if k == 8:
				res.append("Математика и информатика")
			if k == 9:
				res.append("Материалы и современные технологии")

		jsonResult = json.dumps({'result':res})


		return HttpResponse(jsonResult, content_type='application/json')
