# api/mutation.py
import datetime
import graphene
from api.models import RankModel, RankType
 
# Create Mutation 정의
class CreateRank(graphene.Mutation):  
  # 입력받을 파라미터 Field 정의
  class Arguments:
    mode = graphene.String(required=True)
    name = graphene.String(required=True)
    score = graphene.Int(required=True)
    is_mobile = graphene.Boolean(default_value=False) # 생량 가능
 
  # 반환 Field 정의
  rank = graphene.Field(RankType)
  success = graphene.Boolean()
  
  # 실행할 Mutation 정의
  def mutate(root, info, **kwargs):
    # MongoDB Model 생성
    model = RankModel(
      mode=kwargs.get("mode"),
      name=kwargs.get("name"),
      score=kwargs.get("score"),
      is_mobile=kwargs.get("is_mobile"),
      reg_dttm=datetime.datetime.now().strftime("%Y%m%d%H%M%S") # 현재시간
    )
    # MongoDB에 저장
    model.save()
    
    # 결과 반환
    return CreateRank(
      rank=model,
      success=True
    )
 
# Mutation Field 정의
class Mutation(graphene.ObjectType):
  create_rank = CreateRank.Field()