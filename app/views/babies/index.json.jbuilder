json.array!(@babies) do |baby|
  json.extract! baby, :id, :parent1, :parent2, :img1, :img2, :final
  json.url baby_url(baby, format: :json)
end
