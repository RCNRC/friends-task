from .models import UserProfile, User, FriendShip
from rest_framework.views import APIView
from rest_framework.response import Response


class FriendshipStatusAPIView(APIView):
    def get(self, request):
        try:
            to_user = User.objects.get(
                    username=request.query_params['username']
                )
            to_user_profile = UserProfile.objects.get(
                user=to_user,
            )
            from_user_profile = UserProfile.objects.get(
                user=request.user,
            )
            relation_self = from_user_profile.relations.get(to_user=to_user_profile)

            if relation_self.status == 3:
                return Response({'status': 'есть исходящая заявка'})
            elif relation_self.status == 2:
                return Response({'status': 'уже друзья'})
            else:
                return Response({'status': 'есть входящая заявка'})
        except KeyError:
            return Response({'title': 'no user found', 'status': 'failure'}, status=404)
        except User.DoesNotExist:
            return Response({'title': 'server failure', 'status': 'failure'}, status=404)
        except FriendShip.DoesNotExist:
            return Response({'status': 'нет ничего'})


class FriendshipsAPIView(APIView):
    def get(self, request):
        try:
            from_user_profile = UserProfile.objects.get(
                user=request.user,
            )
            relations_self = from_user_profile.relations.all()
            friendships_names = []
            for relation_self in relations_self:
                if relation_self.status == 2:
                    friendships_names.append(relation_self.to_user.user.username)
            return Response({'fiendships': friendships_names})
        except KeyError:
            return Response({'title': 'no user found', 'status': 'failure'}, status=404)
        except User.DoesNotExist:
            return Response({'title': 'server failure', 'status': 'failure'}, status=404)
        except FriendShip.DoesNotExist:
            return Response({'title': 'friendship request does not exists', 'status': 'failure'}, status=404)


class FriendshipRequestsAPIView(APIView):
    def get(self, request):
        try:
            from_user_profile = UserProfile.objects.get(
                user=request.user,
            )
            relations_self = from_user_profile.relations.all()
            income_requests_names = []
            outcome_requests_names = []
            for relation_self in relations_self:
                if relation_self.status == 1:
                    income_requests_names.append(relation_self.to_user.user.username)
                else:
                    outcome_requests_names.append(relation_self.to_user.user.username)
            return Response({'income': income_requests_names, 'outcome': outcome_requests_names})
        except KeyError:
            return Response({'title': 'no user found', 'status': 'failure'}, status=404)
        except User.DoesNotExist:
            return Response({'title': 'server failure', 'status': 'failure'}, status=404)
        except FriendShip.DoesNotExist:
            return Response({'title': 'friendship request does not exists', 'status': 'failure'}, status=404)


class FriendshipRemoveAPIView(APIView):
    def post(self, request):
        try:
            to_user = User.objects.get(
                    username=request.query_params['username']
                )
            to_user_profile = UserProfile.objects.get(
                user=to_user,
            )
            from_user_profile = UserProfile.objects.get(
                user=request.user,
            )
            relation_self = from_user_profile.relations.get(to_user=to_user_profile)
            relation_out = to_user_profile.relations.get(to_user=from_user_profile)

            if relation_out.status == 2:
                relation_self.delete()
                relation_out.delete()
                return Response({'title': 'friendship removed', 'status': 'success'})
            return Response({'title': 'friendship does not exists', 'status': 'failure'}, status=404)
        except KeyError:
            return Response({'title': 'no user found', 'status': 'failure'}, status=404)
        except User.DoesNotExist:
            return Response({'title': 'server failure', 'status': 'failure'}, status=404)
        except FriendShip.DoesNotExist:
            return Response({'title': 'friendship request does not exists', 'status': 'failure'}, status=404)


class FriendshipDeclineAPIView(APIView):
    def post(self, request):
        try:
            to_user = User.objects.get(
                    username=request.query_params['username']
                )
            to_user_profile = UserProfile.objects.get(
                user=to_user,
            )
            from_user_profile = UserProfile.objects.get(
                user=request.user,
            )
            relation_self = from_user_profile.relations.get(to_user=to_user_profile)
            relation_out = to_user_profile.relations.get(to_user=from_user_profile)

            if relation_out.status == 3:
                relation_self.delete()
                relation_out.delete()
                return Response({'title': 'income friendship request declined', 'status': 'success'})
            return Response({'title': 'no income friendship request', 'status': 'failure'}, status=404)
        except KeyError:
            return Response({'title': 'no user found', 'status': 'failure'}, status=404)
        except User.DoesNotExist:
            return Response({'title': 'server failure', 'status': 'failure'}, status=404)
        except FriendShip.DoesNotExist:
            return Response({'title': 'friendship request does not exists', 'status': 'failure'}, status=404)


class FriendshipAcceptAPIView(APIView):
    def post(self, request):
        try:
            to_user = User.objects.get(
                    username=request.query_params['username']
                )
            to_user_profile = UserProfile.objects.get(
                user=to_user,
            )
            from_user_profile = UserProfile.objects.get(
                user=request.user,
            )
            relation_self = from_user_profile.relations.get(to_user=to_user_profile)
            print(relation_self.from_user)
            print(relation_self.status)
            relation_out = to_user_profile.relations.get(to_user=from_user_profile)
            print(relation_out.from_user)
            print(relation_out.status)

            if relation_out.status == 3:
                relation_self.status = 2
                relation_self.save()
                relation_out.status = 2
                relation_out.save()
                return Response({'title': 'friendship activated', 'status': 'success'})
            return Response({'title': 'no income friendship request', 'status': 'failure'}, status=404)
        except KeyError:
            return Response({'title': 'no user found', 'status': 'failure'}, status=404)
        except User.DoesNotExist:
            return Response({'title': 'server failure', 'status': 'failure'}, status=404)
        except FriendShip.DoesNotExist:
            return Response({'title': 'friendship request does not exists', 'status': 'failure'}, status=404)
        

class FriendshipRequestAPIView(APIView):
    def post(self, request):
        try:
            to_user = User.objects.get(
                    username=request.query_params['username']
                )
            to_user_profile = UserProfile.objects.get(
                user=to_user,
            )
            from_user_profile = UserProfile.objects.get(
                user=request.user,
            )

            relation_self = from_user_profile.relations.get(to_user=to_user_profile)
            relation_out = to_user_profile.relations.get(to_user=from_user_profile)

            if relation_out.status == 3:
                relation_self.status = 2
                relation_self.save()
                relation_out.status = 2
                relation_out.save()
                return Response({'title': 'friendship activated', 'status': 'success'})
            return Response({'title': 'friendship or friendship request already exists', 'status': 'failure'}, status=404)
        except KeyError:
            return Response({'title': 'no user found', 'status': 'failure'}, status=404)
        except User.DoesNotExist:
            return Response({'title': 'server failure', 'status': 'failure'}, status=404)
        except FriendShip.DoesNotExist:
            FriendShip.objects.create(
                from_user=from_user_profile,
                to_user=to_user_profile,
                status=3,
            )
            FriendShip.objects.create(
                from_user=to_user_profile,
                to_user=from_user_profile,
                status=1,
            )
            return Response({'title': 'friendship request created', 'status': 'success'})
